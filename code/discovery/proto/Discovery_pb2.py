# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: proto/Discovery.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x15proto/Discovery.proto\"5\n\x10infoMicroservice\x12\x13\n\x0bserviceName\x18\x01 \x01(\t\x12\x0c\n\x04port\x18\x02 \x01(\t\"B\n\x11infoMicroservices\x12-\n\x12microservices_list\x18\x01 \x03(\x0b\x32\x11.infoMicroservice\"D\n\x17microserviceInfoRequest\x12)\n\rmicroservices\x18\x01 \x01(\x0b\x32\x12.infoMicroservices\"B\n\x15microserviceInfoReply\x12)\n\rmicroservices\x18\x01 \x01(\x0b\x32\x12.infoMicroservices\"<\n\nGetRequest\x12\x13\n\x0bserviceName\x18\x01 \x01(\t\x12\x19\n\x11serviceNameTarget\x18\x02 \x01(\t\"-\n\x08GetReply\x12\x13\n\x0bserviceName\x18\x01 \x01(\t\x12\x0c\n\x04port\x18\x02 \x01(\t\"/\n\nPutRequest\x12\x13\n\x0bserviceName\x18\x01 \x01(\t\x12\x0c\n\x04port\x18\x02 \x01(\t\"#\n\x10\x44iscoveryServers\x12\x0f\n\x07servers\x18\x01 \x03(\t\"B\n\x08PutReply\x12\x0e\n\x06result\x18\x01 \x01(\x08\x12&\n\x0blist_server\x18\x02 \x01(\x0b\x32\x11.DiscoveryServers2\x9a\x01\n\x10\x44iscoveryService\x12\x1d\n\x03get\x12\x0b.GetRequest\x1a\t.GetReply\x12\x1d\n\x03put\x12\x0b.PutRequest\x1a\t.PutReply\x12H\n\x14sendMicroserviceInfo\x12\x18.microserviceInfoRequest\x1a\x16.microserviceInfoReplyb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'proto.Discovery_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _INFOMICROSERVICE._serialized_start=25
  _INFOMICROSERVICE._serialized_end=78
  _INFOMICROSERVICES._serialized_start=80
  _INFOMICROSERVICES._serialized_end=146
  _MICROSERVICEINFOREQUEST._serialized_start=148
  _MICROSERVICEINFOREQUEST._serialized_end=216
  _MICROSERVICEINFOREPLY._serialized_start=218
  _MICROSERVICEINFOREPLY._serialized_end=284
  _GETREQUEST._serialized_start=286
  _GETREQUEST._serialized_end=346
  _GETREPLY._serialized_start=348
  _GETREPLY._serialized_end=393
  _PUTREQUEST._serialized_start=395
  _PUTREQUEST._serialized_end=442
  _DISCOVERYSERVERS._serialized_start=444
  _DISCOVERYSERVERS._serialized_end=479
  _PUTREPLY._serialized_start=481
  _PUTREPLY._serialized_end=547
  _DISCOVERYSERVICE._serialized_start=550
  _DISCOVERYSERVICE._serialized_end=704
# @@protoc_insertion_point(module_scope)
