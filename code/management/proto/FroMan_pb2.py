# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: proto/FroMan.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x12proto/FroMan.proto\x12\x05proto\"\xb2\x01\n\tNewFlight\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04\x64\x61te\x18\x02 \x01(\t\x12\x18\n\x10\x64\x65partureAirport\x18\x03 \x01(\t\x12\x16\n\x0e\x61rrivalAirport\x18\x04 \x01(\t\x12\x15\n\rdepartureTime\x18\x05 \x01(\t\x12\x13\n\x0b\x61rrivalTime\x18\x06 \x01(\t\x12\x0f\n\x07\x61irline\x18\x07 \x01(\t\x12\r\n\x05price\x18\x08 \x01(\t\x12\r\n\x05seats\x18\t \x01(\x05\"\x1b\n\x0b\x41\x64\x64Response\x12\x0c\n\x04isOk\x18\x01 \x01(\x08\x32@\n\x0b\x46lightsInfo\x12\x31\n\tAddFlight\x12\x10.proto.NewFlight\x1a\x12.proto.AddResponseb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'proto.FroMan_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _NEWFLIGHT._serialized_start=30
  _NEWFLIGHT._serialized_end=208
  _ADDRESPONSE._serialized_start=210
  _ADDRESPONSE._serialized_end=237
  _FLIGHTSINFO._serialized_start=239
  _FLIGHTSINFO._serialized_end=303
# @@protoc_insertion_point(module_scope)
