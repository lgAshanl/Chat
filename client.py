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

parts = [
    r'(/c)',                   #
    r'(?P<command>\w+)',       # command
    r'(?P<arg>\w*)',           # arg
    r'(?P<args>[a-z, \_ ,\s]*)'     # args
]
pattern = re.compile(r'\s+'.join(parts)+r'\s*\Z')
<<<<<<< HEAD

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
        self.chats_dict = {}
        self.user_hidden = False

        self.server_socket.connectToHost(self.host, self.port, QIODevice.ReadWrite)
        # self.server_socket.waitForConnected(1000)
        # send any message you like it could come from a widget text.
        self.server_socket.readyRead.connect(self.communication)
        self.server_socket.error.connect(self.display_error)

        self.btn_sign_up.clicked.connect(self.sign_up)
        self.btn_sign_in.clicked.connect(self.sign_in)
        # self.textEdit.installEventFilter(self)
        self.btn_send.clicked.connect(self.input_text)

<<<<<<< HEAD
    def _gen_tab(self, tab_name, chat_id):
=======

    def _gen_tab(self, tab_name):
>>>>>>> dev
        tab = QWidget()
        tab.setObjectName(tab_name)
        tab.textBrowser = QTextBrowser(tab)
        tab.textBrowser.setGeometry(QRect(0, 0, 671, 241))
        tab.textBrowser.setObjectName(tab_name+"_tb")
        tab.chat_id = chat_id
        return self.tabWidget.addTab(tab, tab_name)

    def sign_in(self):
        self.user_login = self.line_login.text()
        self.user_passwd = self.line_passwd.text()
        self.user_hidden = self.btn_hide.isChecked()
        self._logging()

        log_info("Sended sing_in package")

    def sign_up(self):
        request = ChatRequest()
        request.command_type = ChatRequest.SIGN_UP
        request.sign.login = self.line_login.text()
        request.sign.passwd = self.line_passwd.text()
        request.sign.hidden = False
        request.successful = True

        qt_send_message(self.server_socket, request.SerializeToString())
        self.user_login = request.sign.login
        self.user_passwd = request.sign.passwd
        self.user_hidden = self.btn_hide.isChecked()

        log_info("Sended sing_up package")

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
                elif user_input["command"] == "add_users":
<<<<<<< HEAD
                    if user_input["arg"] and user_input["args"]:
=======
                    if user_input["arg"]:
>>>>>>> dev
                        self._add_users_to_chat(user_input["arg"]+" "+user_input["args"])
                    else:
                        self.textBrowser.setText("insert chat name and users' names")
                elif user_input["command"] == "answer":
                    if user_input["arg"] and user_input["args"]:
                        current_tab_index = self.tabWidget.currentIndex()
                        current_tab = self.tabWidget.widget(current_tab_index)
                        if current_tab_index:
                            chat_id = current_tab.chat_id
                            self._send_answer(chat_id, int(user_input["arg"]), user_input["args"])
                    else:
                        self.textBrowser.setText("insert message_id and text")
                elif user_input["command"] == "delete_msg":
                    if int(user_input["arg"]):
                        self._send_delete_msg(user_input["arg"])
                    else:
                        self.textBrowser.setText("insert valid message_id")
                else:
                    self.textBrowser.setText("unknown command")
            else:
                # self.textBrowser.append("insert command")
                self.textBrowser.setText("insert command")
        else:
            current_tab_index = self.tabWidget.currentIndex()
            current_tab = self.tabWidget.widget(current_tab_index)
            if current_tab_index:
                chat_id = current_tab.chat_id
                self._send_message(text, chat_id)

    def _add_chat(self, chat_name):
        request = ChatRequest()
        request.command_type = ChatRequest.ADD_CHAT
        request.successful = True
        request.info_text = chat_name
        qt_send_message(self.server_socket, request.SerializeToString())

    def _add_users_to_chat(self, args):
        request = ChatRequest()
        request.command_type = ChatRequest.ADD_USERS_TO_CHAT
        request.successful = True
        request.info_text = args
        qt_send_message(self.server_socket, request.SerializeToString())

    def _get_chats_and_users(self):
        request = ChatRequest()
        request.command_type = ChatRequest.GET_CHATS_AND_MESSAGES
        request.successful = True
        qt_send_message(self.server_socket, request.SerializeToString())

    def _logging(self):
        request = ChatRequest()
        request.command_type = ChatRequest.SIGN_IN
        request.sign.login = self.user_login
        request.sign.passwd = self.user_passwd
        request.sign.hidden = self.user_hidden
        request.successful = True
<<<<<<< HEAD
        qt_send_message(self.server_socket, request.SerializeToString())

    def _send_message(self, text, chat_id):
        request = ChatRequest()
        request.command_type = ChatRequest.MSG
        request.message.chat_id = chat_id
        request.message.text = text
        request.successful = True
        qt_send_message(self.server_socket, request.SerializeToString())

    def _send_answer(self, chat_id, answer_id, text):
        request = ChatRequest()
        request.command_type = ChatRequest.MSG
        request.message.chat_id = chat_id
        request.message.text = text
        request.message.answer_id = answer_id
        request.successful = True
        qt_send_message(self.server_socket, request.SerializeToString())

    def _send_delete_msg(self, msg_id):
        request = ChatRequest()
        request.command_type = ChatRequest.DELETE_MSG
        request.info_text = msg_id
        request.successful = True
=======
>>>>>>> dev
        qt_send_message(self.server_socket, request.SerializeToString())

    def communication(self):
        # data = self.server_socket.readAll()
        data = qt_recv_until_end_messages(self.server_socket)
        if data:
            log_info("recieved {len} bytes from server: {data}".format(
                len=len(data),
                data=data
            ))
            response = ChatResponse()
            response.ParseFromString(data)
            if response.message == "k doc":
                self.dock_login.deleteLater()
                self.dock_login = None
            if response.message == "add":
                self._gen_tab("test_tab")

            if response.command_type == ChatResponse.SIGN_UP:
                if response.successful:
                    print("regged")
                    self._logging()
                else:
                    log_info("bad sing up")
                    print("not regged")
            elif response.command_type == ChatResponse.SIGN_IN:
                if response.successful:
                    print("logged")
                    self._get_chats_and_users()
                else:
                    print("not logged")
                    log_info("bag sing in")
            elif response.command_type == ChatResponse.CHATS_AND_MESSAGES:
                self._gui_add_chats(response.chats)
                self._gui_add_messages(response.messages)
            elif response.command_type == ChatResponse.CHATS:
                self._gui_add_chats(response.chats)
                self._gui_add_messages(response.messages)
            elif response.command_type == ChatResponse.MESSAGES:
                self._gui_add_messages(response.messages)
            else:
                log_info("shit")
                exit(0)
        else:
            print("Disconnected from server")
            sys.exit()

<<<<<<< HEAD
    def _gui_add_chats(self, chats):
        for chat in chats:
            self.chats_dict.update({chat.chat_id: self._gen_tab(chat.chat_name, chat.chat_id)})

    def _gui_add_messages(self, messages):
        for message in messages:
            index = self.chats_dict.get(message.chat_id)
            tab = self.tabWidget.widget(index)
            self._print_message(message, 0, tab)

    def _print_message(self, message, shift, tab):
        tabulation = " " * shift

        text = tabulation + "From {}   {},  id={}".format(
            message.from_name,
            message.time,
            message.message_id)
        # if message.answer.message_id != 0:
        #   text += tabulation + "\nAnswer to "
        if message.file != '':
            text += tabulation + "\nFile to "
        text += "\n{}{}".format(tabulation, message.text)

        tab.textBrowser.append(text)
        if message.answer.message_id != 0:
            text = tabulation + "Answer to "
            tab.textBrowser.append(text)
            self._print_message(message.answer, shift+8, tab)
        if shift == 0:
            tab.textBrowser.append("")

=======
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
