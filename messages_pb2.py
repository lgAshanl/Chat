# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: messages.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='messages.proto',
  package='',
  syntax='proto2',
<<<<<<< HEAD
  serialized_pb=_b('\n\x0emessages.proto\"\xe3\x03\n\x0b\x43hatRequest\x12.\n\x0c\x63ommand_type\x18\x01 \x02(\x0e\x32\x18.ChatRequest.CommandType\x12\x12\n\nsuccessful\x18\x02 \x02(\x08\x12\x11\n\tinfo_text\x18\x03 \x01(\t\x12\x1f\n\x04sign\x18\x04 \x01(\x0b\x32\x11.ChatRequest.Sign\x12%\n\x07message\x18\x05 \x01(\x0b\x32\x14.ChatRequest.Message\x1aI\n\x07Message\x12\x0f\n\x07\x63hat_id\x18\x01 \x02(\x03\x12\x0c\n\x04text\x18\x02 \x02(\t\x12\x11\n\tanswer_id\x18\x03 \x01(\x03\x12\x0c\n\x04\x66ile\x18\x05 \x01(\t\x1a\x35\n\x04Sign\x12\r\n\x05login\x18\x01 \x02(\t\x12\x0e\n\x06passwd\x18\x02 \x02(\t\x12\x0e\n\x06hidden\x18\x03 \x02(\x08\"\xb2\x01\n\x0b\x43ommandType\x12\x07\n\x03MSG\x10\x01\x12\x0f\n\x0bGET_CLIENTS\x10\x02\x12\x1a\n\x16GET_CHATS_AND_MESSAGES\x10\x05\x12\x0b\n\x07SIGN_IN\x10\x06\x12\x0b\n\x07SIGN_UP\x10\x07\x12\x0b\n\x07LOG_OUT\x10\x08\x12\x0c\n\x08\x41\x44\x44_CHAT\x10\t\x12\x15\n\x11\x41\x44\x44_USERS_TO_CHAT\x10\n\x12\x11\n\rBROADCAST_MSG\x10\x0b\x12\x0e\n\nDELETE_MSG\x10\x0c\"\xfa\x03\n\x0c\x43hatResponse\x12\x30\n\x0c\x63ommand_type\x18\x01 \x02(\x0e\x32\x1a.ChatResponse.ResponseType\x12\x12\n\nsuccessful\x18\x02 \x02(\x08\x12\x0f\n\x07message\x18\x03 \x01(\t\x12!\n\x05\x63hats\x18\x04 \x03(\x0b\x32\x12.ChatResponse.Chat\x12\'\n\x08messages\x18\x05 \x03(\x0b\x32\x15.ChatResponse.Message\x1a\x9f\x01\n\x07Message\x12\x12\n\nmessage_id\x18\x01 \x02(\x03\x12\x0f\n\x07\x63hat_id\x18\x02 \x02(\x03\x12\x11\n\tfrom_name\x18\x03 \x02(\t\x12\x0c\n\x04time\x18\x04 \x02(\t\x12\x0b\n\x03tag\x18\x05 \x02(\t\x12\x0c\n\x04text\x18\x06 \x02(\t\x12%\n\x06\x61nswer\x18\x07 \x01(\x0b\x32\x15.ChatResponse.Message\x12\x0c\n\x04\x66ile\x18\x08 \x01(\t\x1a*\n\x04\x43hat\x12\x11\n\tchat_name\x18\x01 \x02(\t\x12\x0f\n\x07\x63hat_id\x18\x02 \x02(\x03\"y\n\x0cResponseType\x12\x11\n\rBROADCAST_MSG\x10\x01\x12\x0b\n\x07\x43LIENTS\x10\x02\x12\x16\n\x12\x43HATS_AND_MESSAGES\x10\x03\x12\t\n\x05\x43HATS\x10\x04\x12\x0c\n\x08MESSAGES\x10\x05\x12\x0b\n\x07SIGN_IN\x10\x06\x12\x0b\n\x07SIGN_UP\x10\x07')
=======
  serialized_pb=_b('\n\x0emessages.proto\"\x90\x02\n\x0b\x43hatRequest\x12.\n\x0c\x63ommand_type\x18\x01 \x02(\x0e\x32\x18.ChatRequest.CommandType\x12\x12\n\nsuccessful\x18\x02 \x02(\x08\x12\x0f\n\x07message\x18\x03 \x01(\t\x12\r\n\x05login\x18\x04 \x01(\t\x12\x0e\n\x06passwd\x18\x05 \x01(\t\x12\x0e\n\x06hidden\x18\x06 \x01(\x08\"}\n\x0b\x43ommandType\x12\x11\n\rBROADCAST_MSG\x10\x01\x12\x0f\n\x0bGET_CLIENTS\x10\x02\x12\x0b\n\x07SIGN_IN\x10\x03\x12\x0b\n\x07SIGN_UP\x10\x04\x12\x0b\n\x07LOG_OUT\x10\x05\x12\x0c\n\x08\x41\x44\x44_CHAT\x10\x06\x12\x15\n\x11\x41\x44\x44_USERS_TO_CHAT\x10\x07\"\xb3\x01\n\x0c\x43hatResponse\x12\x30\n\x0c\x63ommand_type\x18\x01 \x02(\x0e\x32\x1a.ChatResponse.ResponseType\x12\x12\n\nsuccessful\x18\x02 \x02(\x08\x12\x0f\n\x07message\x18\x03 \x01(\t\"L\n\x0cResponseType\x12\x11\n\rBROADCAST_MSG\x10\x01\x12\x0f\n\x0bGET_CLIENTS\x10\x02\x12\x0b\n\x07SIGN_IN\x10\x03\x12\x0b\n\x07SIGN_UP\x10\x04')
>>>>>>> dev
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)



_CHATREQUEST_COMMANDTYPE = _descriptor.EnumDescriptor(
  name='CommandType',
  full_name='ChatRequest.CommandType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='MSG', index=0, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GET_CLIENTS', index=1, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GET_CHATS_AND_MESSAGES', index=2, number=5,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SIGN_IN', index=3, number=6,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SIGN_UP', index=4, number=7,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='LOG_OUT', index=5, number=8,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ADD_CHAT', index=6, number=9,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ADD_USERS_TO_CHAT', index=7, number=10,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BROADCAST_MSG', index=8, number=11,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
<<<<<<< HEAD
      name='DELETE_MSG', index=9, number=12,
=======
      name='ADD_USERS_TO_CHAT', index=6, number=7,
>>>>>>> dev
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
<<<<<<< HEAD
  serialized_start=324,
  serialized_end=502,
=======
  serialized_start=166,
  serialized_end=291,
>>>>>>> dev
)
_sym_db.RegisterEnumDescriptor(_CHATREQUEST_COMMANDTYPE)

_CHATRESPONSE_RESPONSETYPE = _descriptor.EnumDescriptor(
  name='ResponseType',
  full_name='ChatResponse.ResponseType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='BROADCAST_MSG', index=0, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CLIENTS', index=1, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CHATS_AND_MESSAGES', index=2, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CHATS', index=3, number=4,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MESSAGES', index=4, number=5,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SIGN_IN', index=5, number=6,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SIGN_UP', index=6, number=7,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
<<<<<<< HEAD
  serialized_start=890,
  serialized_end=1011,
=======
  serialized_start=397,
  serialized_end=473,
>>>>>>> dev
)
_sym_db.RegisterEnumDescriptor(_CHATRESPONSE_RESPONSETYPE)


_CHATREQUEST_MESSAGE = _descriptor.Descriptor(
  name='Message',
  full_name='ChatRequest.Message',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='chat_id', full_name='ChatRequest.Message.chat_id', index=0,
      number=1, type=3, cpp_type=2, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='text', full_name='ChatRequest.Message.text', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='answer_id', full_name='ChatRequest.Message.answer_id', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='file', full_name='ChatRequest.Message.file', index=3,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=193,
  serialized_end=266,
)

_CHATREQUEST_SIGN = _descriptor.Descriptor(
  name='Sign',
  full_name='ChatRequest.Sign',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='login', full_name='ChatRequest.Sign.login', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='passwd', full_name='ChatRequest.Sign.passwd', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='hidden', full_name='ChatRequest.Sign.hidden', index=2,
      number=3, type=8, cpp_type=7, label=2,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=268,
  serialized_end=321,
)

_CHATREQUEST = _descriptor.Descriptor(
  name='ChatRequest',
  full_name='ChatRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='command_type', full_name='ChatRequest.command_type', index=0,
      number=1, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='successful', full_name='ChatRequest.successful', index=1,
      number=2, type=8, cpp_type=7, label=2,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='info_text', full_name='ChatRequest.info_text', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='sign', full_name='ChatRequest.sign', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='message', full_name='ChatRequest.message', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_CHATREQUEST_MESSAGE, _CHATREQUEST_SIGN, ],
  enum_types=[
    _CHATREQUEST_COMMANDTYPE,
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=19,
  serialized_end=502,
)


_CHATRESPONSE_MESSAGE = _descriptor.Descriptor(
  name='Message',
  full_name='ChatResponse.Message',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='message_id', full_name='ChatResponse.Message.message_id', index=0,
      number=1, type=3, cpp_type=2, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='chat_id', full_name='ChatResponse.Message.chat_id', index=1,
      number=2, type=3, cpp_type=2, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='from_name', full_name='ChatResponse.Message.from_name', index=2,
      number=3, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='time', full_name='ChatResponse.Message.time', index=3,
      number=4, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='tag', full_name='ChatResponse.Message.tag', index=4,
      number=5, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='text', full_name='ChatResponse.Message.text', index=5,
      number=6, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='answer', full_name='ChatResponse.Message.answer', index=6,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='file', full_name='ChatResponse.Message.file', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
<<<<<<< HEAD
  serialized_start=685,
  serialized_end=844,
=======
  serialized_start=19,
  serialized_end=291,
>>>>>>> dev
)

_CHATRESPONSE_CHAT = _descriptor.Descriptor(
  name='Chat',
  full_name='ChatResponse.Chat',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='chat_name', full_name='ChatResponse.Chat.chat_name', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='chat_id', full_name='ChatResponse.Chat.chat_id', index=1,
      number=2, type=3, cpp_type=2, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=846,
  serialized_end=888,
)

_CHATRESPONSE = _descriptor.Descriptor(
  name='ChatResponse',
  full_name='ChatResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='command_type', full_name='ChatResponse.command_type', index=0,
      number=1, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='successful', full_name='ChatResponse.successful', index=1,
      number=2, type=8, cpp_type=7, label=2,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='message', full_name='ChatResponse.message', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='chats', full_name='ChatResponse.chats', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='messages', full_name='ChatResponse.messages', index=4,
      number=5, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_CHATRESPONSE_MESSAGE, _CHATRESPONSE_CHAT, ],
  enum_types=[
    _CHATRESPONSE_RESPONSETYPE,
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
<<<<<<< HEAD
  serialized_start=505,
  serialized_end=1011,
=======
  serialized_start=294,
  serialized_end=473,
>>>>>>> dev
)

_CHATREQUEST_MESSAGE.containing_type = _CHATREQUEST
_CHATREQUEST_SIGN.containing_type = _CHATREQUEST
_CHATREQUEST.fields_by_name['command_type'].enum_type = _CHATREQUEST_COMMANDTYPE
_CHATREQUEST.fields_by_name['sign'].message_type = _CHATREQUEST_SIGN
_CHATREQUEST.fields_by_name['message'].message_type = _CHATREQUEST_MESSAGE
_CHATREQUEST_COMMANDTYPE.containing_type = _CHATREQUEST
_CHATRESPONSE_MESSAGE.fields_by_name['answer'].message_type = _CHATRESPONSE_MESSAGE
_CHATRESPONSE_MESSAGE.containing_type = _CHATRESPONSE
_CHATRESPONSE_CHAT.containing_type = _CHATRESPONSE
_CHATRESPONSE.fields_by_name['command_type'].enum_type = _CHATRESPONSE_RESPONSETYPE
_CHATRESPONSE.fields_by_name['chats'].message_type = _CHATRESPONSE_CHAT
_CHATRESPONSE.fields_by_name['messages'].message_type = _CHATRESPONSE_MESSAGE
_CHATRESPONSE_RESPONSETYPE.containing_type = _CHATRESPONSE
DESCRIPTOR.message_types_by_name['ChatRequest'] = _CHATREQUEST
DESCRIPTOR.message_types_by_name['ChatResponse'] = _CHATRESPONSE

ChatRequest = _reflection.GeneratedProtocolMessageType('ChatRequest', (_message.Message,), dict(

  Message = _reflection.GeneratedProtocolMessageType('Message', (_message.Message,), dict(
    DESCRIPTOR = _CHATREQUEST_MESSAGE,
    __module__ = 'messages_pb2'
    # @@protoc_insertion_point(class_scope:ChatRequest.Message)
    ))
  ,

  Sign = _reflection.GeneratedProtocolMessageType('Sign', (_message.Message,), dict(
    DESCRIPTOR = _CHATREQUEST_SIGN,
    __module__ = 'messages_pb2'
    # @@protoc_insertion_point(class_scope:ChatRequest.Sign)
    ))
  ,
  DESCRIPTOR = _CHATREQUEST,
  __module__ = 'messages_pb2'
  # @@protoc_insertion_point(class_scope:ChatRequest)
  ))
_sym_db.RegisterMessage(ChatRequest)
_sym_db.RegisterMessage(ChatRequest.Message)
_sym_db.RegisterMessage(ChatRequest.Sign)

ChatResponse = _reflection.GeneratedProtocolMessageType('ChatResponse', (_message.Message,), dict(

  Message = _reflection.GeneratedProtocolMessageType('Message', (_message.Message,), dict(
    DESCRIPTOR = _CHATRESPONSE_MESSAGE,
    __module__ = 'messages_pb2'
    # @@protoc_insertion_point(class_scope:ChatResponse.Message)
    ))
  ,

  Chat = _reflection.GeneratedProtocolMessageType('Chat', (_message.Message,), dict(
    DESCRIPTOR = _CHATRESPONSE_CHAT,
    __module__ = 'messages_pb2'
    # @@protoc_insertion_point(class_scope:ChatResponse.Chat)
    ))
  ,
  DESCRIPTOR = _CHATRESPONSE,
  __module__ = 'messages_pb2'
  # @@protoc_insertion_point(class_scope:ChatResponse)
  ))
_sym_db.RegisterMessage(ChatResponse)
_sym_db.RegisterMessage(ChatResponse.Message)
_sym_db.RegisterMessage(ChatResponse.Chat)


# @@protoc_insertion_point(module_scope)
