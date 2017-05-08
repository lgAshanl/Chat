import sys, re
import socket
import select
import time
#from graph.entry import Ui_entry
from gui.Window import Ui_Dialog
from PyQt5.QtCore import QDataStream, QIODevice, QRect
from PyQt5.QtWidgets import * # import QApplication, QDialog, QWidget
from PyQt5.QtNetwork import QTcpSocket, QAbstractSocket

from protocol import qt_send_message, qt_recv_until_end_messages
from messages_pb2 import ChatRequest, ChatResponse

from logging import info as log_info

<<<<<<< HEAD
parts = [
    r'(/c)',                   #
    r'(?P<command>\w+)',       # command
    r'(?P<arg>\w*)',           # arg
    r'(?P<args>[a-z,\s]*)'     # args
]
pattern = re.compile(r'\s+'.join(parts)+r'\s*\Z')
=======
>>>>>>> dev

class ChatClient(Ui_Dialog):
    def __init__(self, dialog,  host, port):
        super().__init__()
        self.setupUi(dialog)
        self.server_socket = QTcpSocket(dialog)
        self.blockSize = 0
        self.server_socket.waitForConnected(1000)
        self.host = host
        self.port = port

        self.server_socket.connectToHost(self.host, self.port, QIODevice.ReadWrite)
        # self.server_socket.waitForConnected(1000)
        # send any message you like it could come from a widget text.
        self.server_socket.readyRead.connect(self.communication)
        self.server_socket.error.connect(self.display_error)

        self.btn_sign_up.clicked.connect(self.sign_up)
        self.btn_sign_in.clicked.connect(self.sign_in)
<<<<<<< HEAD
        # self.textEdit.installEventFilter(self)
        self.btn_send.clicked.connect(self.input_text)

=======
>>>>>>> dev

    def _gen_tab(self, tab_name):
        tab = QWidget()
        tab.setObjectName(tab_name)
        textBrowser = QTextBrowser(tab)
        textBrowser.setGeometry(QRect(0, 0, 671, 251))
        textBrowser.setObjectName("textBrowser")
        textEdit = QTextEdit(tab)
        textEdit.setGeometry(QRect(0, 260, 671, 81))
        textEdit.setObjectName("textEdit")
        btn_send = QPushButton(tab)
        btn_send.setGeometry(QRect(590, 350, 83, 23))
        btn_send.setObjectName("btn_send")
        self.tabWidget.addTab(tab, "OLOLO")

    def sign_in(self):
        self.user_login = self.line_login.text()
        self.user_passwd = self.line_passwd.text()
        self._logging()

        log_info("Sended sing_in package")

    def sign_up(self):
        request = ChatRequest()
        request.command_type = ChatRequest.SIGN_UP
        request.login = self.line_login.text()
        request.passwd = self.line_passwd.text()
        request.successful = True

        qt_send_message(self.server_socket, request.SerializeToString())
        self.user_login = request.login
        self.user_passwd = request.passwd

        log_info("Sended sing_up package")

<<<<<<< HEAD
    def input_text(self):
        text = self.textEdit.toPlainText()
        # command = re.findall(r"/c \w+", text)
        global pattern
        user_input = pattern.match(text+" ")

        if text[0:2] == "/c":
            if user_input is not None:
                user_input.groupdict()
                if user_input["command"] == "add_chat":
                    if user_input["arg"]:
                        self._add_chat(user_input["arg"])
                    else:
                        self.textBrowser.setText("insert name of chat")
                if user_input["command"] == "add_users":
                    if user_input["arg"]:
                        self._add_chat(user_input["arg"]+" "+user_input["args"])
                    else:
                        self.textBrowser.setText("insert chat name")
                else:
                    self.textBrowser.setText("unknown command")
            else:
                # self.textBrowser.append("insert command")
                self.textBrowser.setText("insert command")
        else:
            log_info("Write sending of message")

    def _add_chat(self, chat_name):
        request = ChatRequest()
        request.command_type = ChatRequest.ADD_CHAT
        request.successful = True
        request.message = chat_name
        qt_send_message(self.server_socket, request.SerializeToString())

    def _add_users_to_chat(self, args):
        request = ChatRequest()
        request.command_type = ChatRequest.ADD_USERS_TO_CHAT
        request.successful = True
        request.message = args
        qt_send_message(self.server_socket, request.SerializeToString())

    def _logging(self):
        request = ChatRequest()
        request.command_type = ChatRequest.SIGN_IN
        request.login = self.user_login
        request.passwd = self.user_passwd
        request.successful = True

        qt_send_message(self.server_socket, request.SerializeToString())

    def communication(self):
        #data = self.server_socket.readAll()
        data = qt_recv_until_end_messages(self.server_socket)
        if data:
            print(data)
            response = ChatResponse()
            response.ParseFromString(data)
            print(response.message)
            if response.message == "k doc":
                self.dock_login.deleteLater()
                self.dock_login = None
            if response.message == "add":
                self._gen_tab("test_tab")

            if response.command_type == ChatResponse.SIGN_UP:
                if response.successful:
                    self._logging()
                else:
                    log_info("bad sing up")
                    print(response.message)
            elif response.command_type == ChatResponse.SIGN_UP:
                if response.successful:
                    log_info("")
                else:
                    log_info("bag sing in")
                    print(response.message)

        else:
            print("Disconnected from server")
            sys.exit()

=======
    def _logging(self):
        request = ChatRequest()
        request.command_type = ChatRequest.SIGN_IN
        request.login = self.user_login
        request.passwd = self.user_passwd
        request.successful = True

        qt_send_message(self.server_socket, request.SerializeToString())

    def communication(self):
        #data = self.server_socket.readAll()
        data = qt_recv_until_end_messages(self.server_socket)
        if data:
            print(data)
            response = ChatResponse()
            response.ParseFromString(data)
            print(response.message)
            if response.message == "k doc":
                self.dock_login.deleteLater()
                self.dock_login = None
            if response.message == "add":
                self._gen_tab("test_tab")

            if response.command_type == ChatResponse.SIGN_UP:
                if response.successful:
                    self._logging()
                else:
                    log_info("bad sing up")
                    print(response.message)
            elif response.command_type == ChatResponse.SIGN_UP:
                if response.successful:
                    log_info("")
                else:
                    log_info("bag sing in")
                    print(response.message)

        else:
            print("Disconnected from server")
            sys.exit()

>>>>>>> dev
    def display_error(self, socket_error):
        if socket_error == QAbstractSocket.RemoteHostClosedError:
            pass
        else:
            print(self, "The following error occurred: %s." % self.server_socket.errorString())


def start(host, port):
    import sys

    app = QApplication(sys.argv)
    dialog = QDialog()
    client = ChatClient(dialog, host, port)
    #client.setupUi(dialog)
    dialog.show()
    app.exec_()
