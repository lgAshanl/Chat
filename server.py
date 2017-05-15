import collections
import socket
import select, sys, re
from logging import info as log_info
import datetime
from time import time

from messages_pb2 import ChatRequest, ChatResponse
from protocol import recv_until_end_messages, send_message
import psycopg2


# collections.namedtuple('Client', 'sock addr')
class Client(object):
    def __init__(self, sock, addr):
        self.sock = sock
        self.addr = addr
        self.id = None

    def __str__(self):
        return "Client({})".format(self.addr)


class Container(object):
    pass


class ChatServer(object):
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.connected_clients = []
        self.server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            self.db = psycopg2.connect("dbname='chat_db' user='postgres' host='localhost' password='***'")
            log_info("Connected to {dbname} as {user}, host: {host}".format(
                dbname='chat_db',
                user='postgres',
                host='localhost'
            ))
        except:
            log_info("I am unable to connect to the database")

    def _register_client(self, client):
        self.connected_clients.append(client)

    def _unregister_and_close_client(self, client):
        if client.id is not None:
            self._logout_user(client)
        self.connected_clients.remove(client)
        client.sock.close()

    def _get_client_by_sock(self, sock):
        clients = list(filter(lambda x: x.sock == sock, self.connected_clients))
        assert len(clients) == 1
        return clients[0]

    def _send_message_to_client(self, client, message):
        send_message(client.sock, message)
        log_info("sended {len} bytes to {client}: {data}".format(
            len=len(message),
            client=client,
            data=message
        ))

    def _send_broadcast_message(self, message):
        response = ChatResponse()
        response.successful = True
        response.command_type = ChatResponse.BROADCAST_MSG
        response.info_text = message
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
                        if self._is_user_in_db(request.sign.login):
                            response.successful = False
                            response.message = "This user already exist"
                        else:
                            if request.sign.passwd and request.sign.login:
                                self._add_user_to_db(request.sign.login, request.sign.passwd)
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
                        if self._is_user_in_db(request.sign.login)\
                                and self._login_user(client, request.sign.login, request.sign.passwd, request.sign.hidden):
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
                    elif client.id is not None:
                        if request.command_type == ChatRequest.ADD_CHAT:
<<<<<<< HEAD
                            self._add_chat(client, request.info_text)
                        elif request.command_type == ChatRequest.ADD_USERS_TO_CHAT:
                            self._add_users_to_chat(client, request.info_text)
                        elif request.command_type == ChatRequest.GET_CHATS_AND_MESSAGES:
                            response = ChatResponse()
                            response.command_type = ChatResponse.CHATS_AND_MESSAGES
                            self._get_chats_to_response(client, response.chats)
                            self._get_messages_to_response(response.messages, client.id)
                            response.successful = True
                            self._send_message_to_client(client, response.SerializeToString())
                        elif request.command_type == ChatRequest.MSG:
                            self._broadcast_msg(client, request.message)
                        elif request.command_type == ChatRequest.DELETE_MSG:
                            self._delete_message(client, int(request.info_text))
                        else:
                            log_info("shit")
                    elif client.id is None:
                        self._get_messages_by_chats([])
                        log_info("Client {client}: ohuel".format(
                            client=client,
                        ))
=======
                            self._add_chat(client, request.message)
                        elif request.command_type == ChatRequest.ADD_USERS_TO_CHAT:
                            self._add_users_to_chat(client, request.message)
>>>>>>> dev
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
        self.db.commit()

    def _add_chat(self, client, arg):
        chat_name = re.search(r'\w+', arg).group(0)
        cursor = self.db.cursor()

        cursor.execute("SELECT * FROM chats "
                       "WHERE name = %s and admin_id = %s "
                       "LIMIT 1;",
                       (chat_name, client.id,))
        rows = cursor.fetchall()
        if not len(rows):
            cursor.execute("INSERT INTO chats (admin_id, name) "
                           "VALUES (%s, %s);",
                           (client.id, chat_name,))
            cursor.execute("SELECT * FROM chats "
                           "WHERE name = %s and admin_id = %s "
                           "LIMIT 1;",
                           (chat_name, client.id,))
            rows = cursor.fetchall()
            chat_id = rows[0][0]
            cursor.execute("INSERT INTO chat_users (user_id, chat_id, hidden) "
                           "VALUES (%s, %s, %s);",
                           (client.id, chat_id, False))
            self._send_chat(client.id, chat_id)
            self.db.commit()

    def _add_users_to_chat(self, client, args):
        names = re.findall(r'\w+', args)
        chat_name = names[0]
        names = names[1:]

        cursor = self.db.cursor()
        cursor.execute("SELECT chats.chat_id FROM chats INNER JOIN chat_users "
                       "ON chats.chat_id = chat_users.chat_id "
                       "WHERE name = %s and user_id = %s "
                       "LIMIT 1;",
                       (chat_name, client.id,))
        rows = cursor.fetchall()
        if len(rows):
            chat_id = rows[0][0]
            for user in names:
                cursor.execute("SELECT user_id FROM users "
                               "WHERE name = %s "
                               "LIMIT 1;",
                               (user,))
                rows = cursor.fetchall()
                user_id = rows[0][0]
                cursor.execute("INSERT INTO chat_users (user_id, chat_id, hidden) "
                               "VALUES (%s, %s, %s);",
                               (user_id, chat_id, False))
                self._send_chat(user_id, chat_id)
            self.db.commit()

    def _get_set_of_deleted_messages(self, client_id):
        cursor = self.db.cursor()
        cursor.execute("SELECT message_id FROM deleted_messages "
                       "WHERE user_id = %s;",
                       (client_id,))
        rows = cursor.fetchall()
        deleted_msg = set()
        for x in rows:
            deleted_msg.update([x[0]])
        return deleted_msg

    def _get_chats_by_id(self, id):
        cursor = self.db.cursor()
        cursor.execute("SELECT chats.chat_id AS chat_id, name "
                       "FROM chats INNER JOIN chat_users "
                       "            ON chats.chat_id = chat_users.chat_id "
                       "WHERE user_id = %s;",
                       (id,))
        rows = cursor.fetchall()
        chats = []
        for x in rows:
            chats.append(tuple([x[0], x[1]]))
        return chats

    def _get_user_id_by_user_name(self, user_name):
        cursor = self.db.cursor()
        cursor.execute("SELECT user_id FROM users "
                       "WHERE name = %s "
                       "LIMIT 1;",
                       (user_name,))
        rows = cursor.fetchall()
        return rows[0][0]

    def _get_user_name_by_user_id(self, user_id):
        cursor = self.db.cursor()
        cursor.execute("SELECT name FROM users "
                       "WHERE user_id = %s "
                       "LIMIT 1;",
                       (user_id,))
        rows = cursor.fetchall()
        return rows[0][0]

    def _get_messages_by_chats(self, chats):
        chats = tuple(chats)
        chat_ids = []
        for x in chats:
            chat_ids.append(x[0])
        chat_ids = tuple(chat_ids)
        if not chat_ids:
            return []
        cursor = self.db.cursor()
        cursor.execute("SELECT 	messages.message_id, chats.chat_id AS chat, users.name AS author, "
                       "        time, tag, text, answer_id, file_id "
                       "FROM chats "
                       "INNER JOIN messages "
                       "    ON chats.chat_id = messages.chat_id "
                       "INNER JOIN users "
                       "    ON users.user_id = messages.from_id "
                       "WHERE chats.chat_id IN %s "
                       "ORDER BY time;",
                       (chat_ids,))
        rows = cursor.fetchall()
        return rows

    def _get_users_by_chat(self, chat_id):
        cursor = self.db.cursor()
        cursor.execute("SELECT 	user_id "
                       "FROM chat_users "
                       "WHERE chat_id = %s ",
                       (chat_id,))
        rows = cursor.fetchall()
        users = set()
        for x in rows:
            users.add(x[0])
        return users

    def _get_chats_to_response(self, client, response_chats):
        for x in self._get_chats_by_id(client.id):
            chat = response_chats.add()
            chat.chat_id = x[0]
            chat.chat_name = x[1]

    def _get_message_id_by_answer_id(self, answer_id):
        cursor = self.db.cursor()
        cursor.execute("SELECT to_id "
                       "FROM answers "
                       "WHERE answer_id = %s;",
                       (answer_id, ))
        rows = cursor.fetchall()
        if len(rows):
            message_id = rows[0][0]
            return message_id
        return -1

    def _get_messages_to_response(self, response_messages, client_id=0, chats=None):
        deleted_msg = set()
        if chats is None:
            chats = self._get_chats_by_id(client_id)
            deleted_msg = self._get_set_of_deleted_messages(client_id)
        for x in self._get_messages_by_chats(chats):
            if x[0] in deleted_msg:
                continue
            mes = response_messages.add()
            mes.message_id = x[0]
            mes.chat_id = x[1]
            mes.from_name = x[2]
            mes.time = str(x[3])
            mes.tag = x[4]
            mes.text = x[5]
            if x[6] is not None:
                mes_id = self._get_message_id_by_answer_id(x[6])
                if mes_id >= 0:
                    self._preparing_sub_message(mes_id, mes.answer)
                # mes.answer = x[6]
            if x[7] is not None:
                mes.file = x[7]

    def _is_user_in_chat(self, user_id, chat_id):
        cursor = self.db.cursor()
        cursor.execute("SELECT user_id FROM chat_users "
                        "WHERE user_id = %s AND chat_id = %s "
                        "LIMIT 1;",
                        (user_id, chat_id,))
        rows = cursor.fetchall()
        return bool(len(rows))

    def _preparing_sub_message(self, message_id, sub_mes):
        cursor = self.db.cursor()
        cursor.execute("SELECT * FROM messages "
                       "WHERE message_id = %s "
                       "LIMIT 1;",
                       (message_id,))
        rows = cursor.fetchall()

        if not len(rows):
            return

        sub_mes.message_id = message_id
        sub_mes.chat_id = rows[0][1]
        sub_mes.from_name = self._get_user_name_by_user_id(rows[0][3])
        sub_mes.time = str(rows[0][4])
        sub_mes.tag = rows[0][5]
        sub_mes.text = rows[0][6]
        if rows[0][7]:
            cursor.execute("SELECT to_id "
                           "FROM answers "
                           "WHERE answer_id = %s "
                           "LIMIT 1;",
                           (rows[0][7],))
            ans_id = cursor.fetchall()
            self._preparing_sub_message(ans_id[0][0], sub_mes.answer)
        if rows[0][8]:
            sub_mes.file_id = str(rows[0][8])

    def _preparing_message_for_db(self, client, request):
        cursor = self.db.cursor()
        cursor.execute("SELECT name FROM users "
                       "WHERE user_id = %s "
                       "LIMIT 1;",
                       (client.id,))
        rows = cursor.fetchall()

        mes = Container()
        # mes.chat_id = lambda: None
        mes.chat_id = request.chat_id
        mes.ip = client.addr[0]
        mes.from_id = client.id
        mes.from_name = rows[0][0]
        mes.time = datetime.datetime.fromtimestamp(time()).strftime('%Y-%m-%d %H:%M:%S')
        mes.tag = 'message'
        mes.text = request.text
        if request.answer_id == 0:
            mes.answer_id = None
        else:
            mes.answer_id = request.answer_id
        mes.file_id = None
        return mes

    def _preparing_message_for_response(self, p_message):
        response = ChatResponse()
        response.command_type = ChatResponse.MESSAGES
        mes = response.messages.add()
        mes.message_id = p_message.message_id
        mes.chat_id = p_message.chat_id
        mes.from_name = p_message.from_name
        mes.time = p_message.time
        mes.tag = p_message.tag
        mes.text = p_message.text
        if p_message.answer_id is not None:
            mes_id = self._get_message_id_by_answer_id(p_message.answer_id)
            if mes_id >= 0:
                self._preparing_sub_message(mes_id, mes.answer)
        if p_message.file_id is not None:
            mes.file = str(p_message.file_id)
        response.successful = True
        return response

    def _preparing_chat_for_response(self, chat_id, chat_name):
        response = ChatResponse()
        response.command_type = ChatResponse.CHATS
        chat = response.chats.add()
        chat.chat_id = chat_id
        chat.chat_name = chat_name
        response.successful = True
        return response

<<<<<<< HEAD
    def _add_message_to_db(self, message):
        cursor = self.db.cursor()
        cursor.execute("INSERT INTO messages (chat_id, ip, from_id, "
                       "time, tag, text, answer_id, file_id) "
                       "VALUES (%s, %s, %s, %s, %s, %s, %s, %s);",
                        (message.chat_id, message.ip, message.from_id,
                         message.time, message.tag, message.text,
                         None,
                         message.file_id,))
        self.db.commit()
        cursor.execute("SELECT lastval();")
        rows = cursor.fetchall()
        message.message_id = rows[0][0]
        return message.message_id

    def _add_answer_to_db(self, to_id, p_message):
        cursor = self.db.cursor()
        cursor.execute("INSERT INTO answers (to_id) "
                       "VALUES (%s);",
                       (to_id,))
        self.db.commit()
        cursor.execute("SELECT lastval();")
        rows = cursor.fetchall()
        p_message.answer_id = rows[0][0]

        cursor.execute("UPDATE messages "
                       "SET answer_id = %s "
                       "WHERE message_id = %s;",
                       (p_message.answer_id, p_message.message_id,))
        self.db.commit()
        # return p_message.answere_id

    def _broadcast_msg(self, client, request):
        if self._is_user_in_chat(client.id, request.chat_id):
            p_message = self._preparing_message_for_db(client, request)
            self._add_message_to_db(p_message)
            if p_message.answer_id is not None:
                self._add_answer_to_db(request.answer_id, p_message)
            response = self._preparing_message_for_response(p_message)
            response = response.SerializeToString()
            for client in self.connected_clients:
                if client.id in self._get_users_by_chat(p_message.chat_id):
                    self._send_message_to_client(client, response)

        else:
            log_info("Client {client}: ohuel".format(
                client=client,
            ))

    def _delete_message(self, client, msg_id):
        cursor = self.db.cursor()
        cursor.execute("INSERT INTO deleted_messages (user_id, message_id) "
                       "VALUES (%s, %s);",
                       (client.id, msg_id,))
        self.db.commit()

    def _send_chat(self, user_id, chat_id):
        cursor = self.db.cursor()
        cursor.execute("SELECT name "
                       "FROM chats INNER JOIN chat_users "
                       "            ON chats.chat_id = chat_users.chat_id "
                       "WHERE user_id = %s AND chats.chat_id = %s;",
                       (user_id, chat_id,))
        rows = cursor.fetchall()
        chat_name = rows[0][0]
        response = self._preparing_chat_for_response(chat_id, chat_name)
        self._get_messages_to_response(response.messages, chats=[[chat_id]])
        response = response.SerializeToString()
        for client in self.connected_clients:
            if client.id == user_id:
                self._send_message_to_client(client, response)
                break
=======
    def _add_chat(self, client, arg):
        chat_name = re.search(r'\w+', arg).group(0)
        cursor = self.db.cursor()

        cursor.execute("SELECT * FROM chats "
                       "WHERE name = %s and admin_id = %s "
                       "LIMIT 1;",
                       (chat_name, client.id,))
        rows = cursor.fetchall()
        if not len(rows):
            cursor.execute("INSERT INTO chats (admin_id, name) "
                           "VALUES (%s, %s);",
                           (client.id, chat_name,))
            cursor.execute("SELECT * FROM chats "
                           "WHERE name = %s and admin_id = %s "
                           "LIMIT 1;",
                           (chat_name, client.id,))
            rows = cursor.fetchall()
            cursor.execute("INSERT INTO chat_users (user_id, chat_id, hidden) "
                           "VALUES (%s, %s, %s);",
                           (client.id, rows[0][0], False))
            self.db.commit()

    def _add_users_to_chat(self, client, args):
        names = re.findall(r'\w+', args)
        chat_name = names[0]
        names = names[1:]

        cursor = self.db.cursor()

        cursor.execute("SELECT chats.chat_id FROM chats INNER JOIN chat_users "
                       "ON chats.chat_id = chat_users.chat_id "
                       "WHERE name = %s and user_id = %s "
                       "LIMIT 1;",
                       (chat_name, client.id,))
        rows = cursor.fetchall()
        if len(rows):
            chat_id = rows[0][0]
            for user in names:
                cursor.execute("SELECT user_id FROM users "
                               "WHERE name = %s "
                               "LIMIT 1;",
                               (user,))
                rows = cursor.fetchall()
                user_id = rows[0][0]
                cursor.execute("INSERT INTO chat_users (user_id, chat_id, hidden) "
                               "VALUES (%s, %s, %s);",
                               (user_id, chat_id, False))
            self.db.commit()


>>>>>>> dev

    def start(self):
        self.server_sock.bind((self.host, self.port))
        log_info("Server started")
        self.server_sock.listen(10)
        try:
            self._input_loop()
        finally:
            self.server_sock.close()
