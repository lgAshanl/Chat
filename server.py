import collections
import socket
import select, sys
from logging import info as log_info

from messages_pb2 import ChatRequest, ChatResponse
from protocol import recv_until_end_messages, send_message
import psycopg2


# collections.namedtuple('Client', 'sock addr')
class Client(object):
    def __init__(self, sock, addr):
        self.sock = sock
        self.addr = addr

    def __str__(self):
        return "Client({})".format(self.addr)


class ChatServer(object):
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.connected_clients = []
        self.server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            self.db = psycopg2.connect("dbname='test_db' user='postgres' host='localhost' password='***'")
            log_info("Connected to {dbname} as {user}, host: {host}".format(
                dbname='test_db',
                user='postgres',
                host='localhost'
            ))
        except:
            log_info("I am unable to connect to the database")

    def _register_client(self, client):
        self.connected_clients.append(client)

    def _unregister_and_close_client(self, client):
        self._logout_user(client)
        self.connected_clients.remove(client)
        client.sock.close()

    def _get_client_by_sock(self, sock):
        clients = list(filter(lambda x: x.sock == sock, self.connected_clients))
        assert len(clients) == 1
        return clients[0]

    def _send_message_to_client(self, client, message):
        send_message(client.sock, message)

    def _send_broadcast_message(self, message):
        response = ChatResponse()
        response.successful = True
        response.command_type = ChatResponse.BROADCAST_MSG
        response.message = message
        for client in self.connected_clients:
            self._send_message_to_client(client, response.SerializeToString())

    def _input_loop(self):
        while True:
            socks_to_read = list(map(lambda x: x.sock, self.connected_clients))

            # Linux epoll magic
            socks_ready_to_read, _, _ = select.select([self.server_sock] + socks_to_read, [], [])

            for sock in socks_ready_to_read:
                if sock == self.server_sock:
                    sock, addr = self.server_sock.accept()
                    new_client = Client(sock=sock, addr=addr)
                    self._register_client(new_client)

                    log_info("{} connected".format(str(new_client)))
                else:
                    client = self._get_client_by_sock(sock)
                    data = recv_until_end_messages(client.sock)
                    if not data:
                        self._unregister_and_close_client(client)
                        log_info("{} is offline (initiated by the client)".format(str(client)))
                        continue

                    log_info("recieved {len} bytes from {client}: {data}".format(
                        len=len(data),
                        client=client,
                        data=data
                    ))

                    request = ChatRequest()
                    request.ParseFromString(data)
                    if request.command_type == ChatRequest.BROADCAST_MSG:
                        print("message=", request.message)
                        if request.message == "":
                            request.message = "test_message"
                        self._send_broadcast_message(request.message)
                    elif request.command_type == ChatRequest.GET_CLIENTS:
                        self._send_broadcast_message(str(self.connected_clients).encode())
                    elif request.command_type == ChatRequest.SIGN_UP:
                        response = ChatResponse()
                        response.command_type = ChatResponse.SIGN_UP
                        if self._is_user_in_db(request.login):
                            response.successful = False
                            response.message = "This user already exist"
                        else:
                            if request.passwd and request.login:
                                self._add_user_to_db(request.login, request.passwd)
                                response.successful = True
                                response.message = "You registered"
                            else:
                                response.successful = False
                                response.message = "Insert password and login, bastard"

                        self._send_message_to_client(client, response.SerializeToString())

                        log_info("SING_UP:{} is {} (initiated by the client)\n\t\t{}".format(
                            str(client),
                            str(response.successful),
                            response.message
                        ))
                    elif request.command_type == ChatRequest.SIGN_IN:
                        response = ChatResponse()
                        response.command_type = ChatResponse.SIGN_IN
                        if self._is_user_in_db(request.login)\
                                and self._login_user(client, request.login, request.passwd, request.hidden):
                            response.successful = True
                            response.message = "You logged"
                        else:
                            response.successful = False
                            response.message = "This user dose not already exist or wrong login/password"

                        self._send_message_to_client(client, response.SerializeToString())

                        log_info("SING_IN:{} is {} (initiated by the client)\n\t\t{}".format(
                            str(client),
                            str(response.successful),
                            response.message
                        ))
                    else:
                        log_info("shit")
                        exit(0)

    def _is_user_in_db(self, login):
        cursor = self.db.cursor()
        cursor.execute("SELECT * FROM users WHERE name = %s;", (login,))
        rows = cursor.fetchall()

        return bool(len(rows))

    def _add_user_to_db(self, login, passwd):
        cursor = self.db.cursor()
        cursor.execute("INSERT INTO users (name, status, hidden, password) "
                       "VALUES (%s, %s, %s, %s);",
                       (login, False, False, passwd,))
        self.db.commit()

    def _login_user(self, client, login, passwd, hidden):
        # UPDATE products SET price = 10 WHERE price = 5;
        cursor = self.db.cursor()
        cursor.execute("SELECT * FROM users WHERE name = %s and password = %s;", (login, passwd,))
        rows = cursor.fetchall()

        if not bool(len(rows)):
            log_info("{} wrong passwd".format(login))
            return False

        client.id = rows[0][0]
        if hidden is None:
            hidden = False
        cursor.execute("UPDATE users "
                       "SET status = true, hidden = %s "
                       "WHERE name = %s;",
                       (hidden, login,))
        self.db.commit()
        return True

    def _logout_user(self, client):
        cursor = self.db.cursor()
        cursor.execute("UPDATE users "
                       "SET status = true, hidden = false "
                       "WHERE user_id = %s;",
                       (client.id,))


    def start(self):
        self.server_sock.bind((self.host, self.port))
        log_info("Server started")
        self.server_sock.listen(10)
        try:
            self._input_loop()
        finally:
            self.server_sock.close()
