# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: proto/FroReg.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x12proto/FroReg.proto\x12\x05proto\"\x88\x01\n\nSignUpInfo\x12\r\n\x05\x65mail\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x0f\n\x07surname\x18\x03 \x01(\t\x12\x10\n\x08password\x18\x04 \x01(\t\x12\x17\n\x0fpasswordConfirm\x18\x05 \x01(\t\x12\x10\n\x08userType\x18\x06 \x01(\t\x12\x0f\n\x07\x61irline\x18\x07 \x01(\t\"\x1e\n\x0eSignUpResponse\x12\x0c\n\x04isOk\x18\x01 \x01(\x08\".\n\x0b\x43redentials\x12\r\n\x05\x65mail\x18\x01 \x01(\t\x12\x10\n\x08password\x18\x02 \x01(\t\"V\n\x0eSignInResponse\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0f\n\x07surname\x18\x02 \x01(\t\x12\x12\n\nstoredType\x18\x03 \x01(\t\x12\x11\n\tisCorrect\x18\x04 \x01(\x08\x32t\n\tUsersInfo\x12\x32\n\x06SignUp\x12\x11.proto.SignUpInfo\x1a\x15.proto.SignUpResponse\x12\x33\n\x06SignIn\x12\x12.proto.Credentials\x1a\x15.proto.SignInResponseb\x06proto3')



_SIGNUPINFO = DESCRIPTOR.message_types_by_name['SignUpInfo']
_SIGNUPRESPONSE = DESCRIPTOR.message_types_by_name['SignUpResponse']
_CREDENTIALS = DESCRIPTOR.message_types_by_name['Credentials']
_SIGNINRESPONSE = DESCRIPTOR.message_types_by_name['SignInResponse']
SignUpInfo = _reflection.GeneratedProtocolMessageType('SignUpInfo', (_message.Message,), {
  'DESCRIPTOR' : _SIGNUPINFO,
  '__module__' : 'proto.FroReg_pb2'
  # @@protoc_insertion_point(class_scope:proto.SignUpInfo)
  })
_sym_db.RegisterMessage(SignUpInfo)

SignUpResponse = _reflection.GeneratedProtocolMessageType('SignUpResponse', (_message.Message,), {
  'DESCRIPTOR' : _SIGNUPRESPONSE,
  '__module__' : 'proto.FroReg_pb2'
  # @@protoc_insertion_point(class_scope:proto.SignUpResponse)
  })
_sym_db.RegisterMessage(SignUpResponse)

Credentials = _reflection.GeneratedProtocolMessageType('Credentials', (_message.Message,), {
  'DESCRIPTOR' : _CREDENTIALS,
  '__module__' : 'proto.FroReg_pb2'
  # @@protoc_insertion_point(class_scope:proto.Credentials)
  })
_sym_db.RegisterMessage(Credentials)

SignInResponse = _reflection.GeneratedProtocolMessageType('SignInResponse', (_message.Message,), {
  'DESCRIPTOR' : _SIGNINRESPONSE,
  '__module__' : 'proto.FroReg_pb2'
  # @@protoc_insertion_point(class_scope:proto.SignInResponse)
  })
_sym_db.RegisterMessage(SignInResponse)

_USERSINFO = DESCRIPTOR.services_by_name['UsersInfo']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _SIGNUPINFO._serialized_start=30
  _SIGNUPINFO._serialized_end=166
  _SIGNUPRESPONSE._serialized_start=168
  _SIGNUPRESPONSE._serialized_end=198
  _CREDENTIALS._serialized_start=200
  _CREDENTIALS._serialized_end=246
  _SIGNINRESPONSE._serialized_start=248
  _SIGNINRESPONSE._serialized_end=334
  _USERSINFO._serialized_start=336
  _USERSINFO._serialized_end=452
# @@protoc_insertion_point(module_scope)
