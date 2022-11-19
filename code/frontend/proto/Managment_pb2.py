# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: proto/Managment.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x15proto/Managment.proto\x12\x05proto\"$\n\x0fSeatCostRequest\x12\x11\n\tcompagnia\x18\x01 \x01(\t\"\x1f\n\rSeatCostReply\x12\x0e\n\x06prezzo\x18\x01 \x01(\t\"1\n\x1c\x41\x64\x64itionalServiceCostRequest\x12\x11\n\tcompagnia\x18\x01 \x01(\t\",\n\x1a\x41\x64\x64itionalServiceCostReply\x12\x0e\n\x06prezzo\x18\x01 \x01(\t\"\x1e\n\x0cPriceRequest\x12\x0e\n\x06idVolo\x18\x01 \x01(\t\"\x1b\n\nPriceReply\x12\r\n\x05price\x18\x01 \x01(\t\"\xb2\x01\n\tNewFlight\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04\x64\x61te\x18\x02 \x01(\t\x12\x18\n\x10\x64\x65partureAirport\x18\x03 \x01(\t\x12\x16\n\x0e\x61rrivalAirport\x18\x04 \x01(\t\x12\x15\n\rdepartureTime\x18\x05 \x01(\t\x12\x13\n\x0b\x61rrivalTime\x18\x06 \x01(\t\x12\x0f\n\x07\x61irline\x18\x07 \x01(\t\x12\r\n\x05price\x18\x08 \x01(\t\x12\r\n\x05seats\x18\t \x01(\x05\"*\n\x0b\x41\x64\x64Response\x12\x0c\n\x04isOk\x18\x01 \x01(\x08\x12\r\n\x05\x65rror\x18\x02 \x01(\t\"3\n\rUpdatedFlight\x12\x10\n\x08\x66lightId\x18\x01 \x01(\t\x12\x10\n\x08newPrice\x18\x02 \x01(\t\"0\n\x11ModFlightResponse\x12\x0c\n\x04isOk\x18\x01 \x01(\x08\x12\r\n\x05\x65rror\x18\x02 \x01(\t\"q\n\x0cUpdatedSeats\x12\x0f\n\x07\x61irline\x18\x01 \x01(\t\x12\x0e\n\x06price1\x18\x02 \x01(\t\x12\x0e\n\x06price2\x18\x03 \x01(\t\x12\x0e\n\x06price6\x18\x04 \x01(\t\x12\x0f\n\x07price16\x18\x05 \x01(\t\x12\x0f\n\x07price18\x18\x06 \x01(\t\"/\n\x10ModSeatsResponse\x12\x0c\n\x04isOk\x18\x01 \x01(\x08\x12\r\n\x05\x65rror\x18\x02 \x01(\t\"\x88\x01\n\x0fUpdatedServices\x12\x0f\n\x07\x61irline\x18\x01 \x01(\t\x12\x0f\n\x07priceBM\x18\x02 \x01(\t\x12\x0f\n\x07priceBG\x18\x03 \x01(\t\x12\x0f\n\x07priceBS\x18\x04 \x01(\t\x12\x0f\n\x07priceAD\x18\x05 \x01(\t\x12\x0f\n\x07priceAB\x18\x06 \x01(\t\x12\x0f\n\x07priceTN\x18\x07 \x01(\t\"2\n\x13ModServicesResponse\x12\x0c\n\x04isOk\x18\x01 \x01(\x08\x12\r\n\x05\x65rror\x18\x02 \x01(\t\",\n\x14GetLogFileRequestMan\x12\x14\n\x0cnumRichiesta\x18\x01 \x01(\x05\";\n\x12GetLogFileReplyMan\x12\x12\n\nchunk_file\x18\x01 \x01(\x0c\x12\x11\n\tnum_chunk\x18\x02 \x01(\x05\x32\xb9\x04\n\x0b\x46lightsInfo\x12\x31\n\tAddFlight\x12\x10.proto.NewFlight\x1a\x12.proto.AddResponse\x12>\n\x0cModifyFlight\x12\x14.proto.UpdatedFlight\x1a\x18.proto.ModFlightResponse\x12;\n\x0bModifySeats\x12\x13.proto.UpdatedSeats\x1a\x17.proto.ModSeatsResponse\x12\x44\n\x0eModifyServices\x12\x16.proto.UpdatedServices\x1a\x1a.proto.ModServicesResponse\x12\x38\n\x0eGetPriceFlight\x12\x13.proto.PriceRequest\x1a\x11.proto.PriceReply\x12\x43\n\x11GetAllSeatsFlight\x12\x16.proto.SeatCostRequest\x1a\x14.proto.SeatCostReply0\x01\x12j\n\x1eGetAlladditionalServicesFlight\x12#.proto.AdditionalServiceCostRequest\x1a!.proto.AdditionalServiceCostReply0\x01\x12I\n\rgetLogFileMan\x12\x1b.proto.GetLogFileRequestMan\x1a\x19.proto.GetLogFileReplyMan0\x01\x62\x06proto3')



_SEATCOSTREQUEST = DESCRIPTOR.message_types_by_name['SeatCostRequest']
_SEATCOSTREPLY = DESCRIPTOR.message_types_by_name['SeatCostReply']
_ADDITIONALSERVICECOSTREQUEST = DESCRIPTOR.message_types_by_name['AdditionalServiceCostRequest']
_ADDITIONALSERVICECOSTREPLY = DESCRIPTOR.message_types_by_name['AdditionalServiceCostReply']
_PRICEREQUEST = DESCRIPTOR.message_types_by_name['PriceRequest']
_PRICEREPLY = DESCRIPTOR.message_types_by_name['PriceReply']
_NEWFLIGHT = DESCRIPTOR.message_types_by_name['NewFlight']
_ADDRESPONSE = DESCRIPTOR.message_types_by_name['AddResponse']
_UPDATEDFLIGHT = DESCRIPTOR.message_types_by_name['UpdatedFlight']
_MODFLIGHTRESPONSE = DESCRIPTOR.message_types_by_name['ModFlightResponse']
_UPDATEDSEATS = DESCRIPTOR.message_types_by_name['UpdatedSeats']
_MODSEATSRESPONSE = DESCRIPTOR.message_types_by_name['ModSeatsResponse']
_UPDATEDSERVICES = DESCRIPTOR.message_types_by_name['UpdatedServices']
_MODSERVICESRESPONSE = DESCRIPTOR.message_types_by_name['ModServicesResponse']
_GETLOGFILEREQUESTMAN = DESCRIPTOR.message_types_by_name['GetLogFileRequestMan']
_GETLOGFILEREPLYMAN = DESCRIPTOR.message_types_by_name['GetLogFileReplyMan']
SeatCostRequest = _reflection.GeneratedProtocolMessageType('SeatCostRequest', (_message.Message,), {
  'DESCRIPTOR' : _SEATCOSTREQUEST,
  '__module__' : 'proto.Managment_pb2'
  # @@protoc_insertion_point(class_scope:proto.SeatCostRequest)
  })
_sym_db.RegisterMessage(SeatCostRequest)

SeatCostReply = _reflection.GeneratedProtocolMessageType('SeatCostReply', (_message.Message,), {
  'DESCRIPTOR' : _SEATCOSTREPLY,
  '__module__' : 'proto.Managment_pb2'
  # @@protoc_insertion_point(class_scope:proto.SeatCostReply)
  })
_sym_db.RegisterMessage(SeatCostReply)

AdditionalServiceCostRequest = _reflection.GeneratedProtocolMessageType('AdditionalServiceCostRequest', (_message.Message,), {
  'DESCRIPTOR' : _ADDITIONALSERVICECOSTREQUEST,
  '__module__' : 'proto.Managment_pb2'
  # @@protoc_insertion_point(class_scope:proto.AdditionalServiceCostRequest)
  })
_sym_db.RegisterMessage(AdditionalServiceCostRequest)

AdditionalServiceCostReply = _reflection.GeneratedProtocolMessageType('AdditionalServiceCostReply', (_message.Message,), {
  'DESCRIPTOR' : _ADDITIONALSERVICECOSTREPLY,
  '__module__' : 'proto.Managment_pb2'
  # @@protoc_insertion_point(class_scope:proto.AdditionalServiceCostReply)
  })
_sym_db.RegisterMessage(AdditionalServiceCostReply)

PriceRequest = _reflection.GeneratedProtocolMessageType('PriceRequest', (_message.Message,), {
  'DESCRIPTOR' : _PRICEREQUEST,
  '__module__' : 'proto.Managment_pb2'
  # @@protoc_insertion_point(class_scope:proto.PriceRequest)
  })
_sym_db.RegisterMessage(PriceRequest)

PriceReply = _reflection.GeneratedProtocolMessageType('PriceReply', (_message.Message,), {
  'DESCRIPTOR' : _PRICEREPLY,
  '__module__' : 'proto.Managment_pb2'
  # @@protoc_insertion_point(class_scope:proto.PriceReply)
  })
_sym_db.RegisterMessage(PriceReply)

NewFlight = _reflection.GeneratedProtocolMessageType('NewFlight', (_message.Message,), {
  'DESCRIPTOR' : _NEWFLIGHT,
  '__module__' : 'proto.Managment_pb2'
  # @@protoc_insertion_point(class_scope:proto.NewFlight)
  })
_sym_db.RegisterMessage(NewFlight)

AddResponse = _reflection.GeneratedProtocolMessageType('AddResponse', (_message.Message,), {
  'DESCRIPTOR' : _ADDRESPONSE,
  '__module__' : 'proto.Managment_pb2'
  # @@protoc_insertion_point(class_scope:proto.AddResponse)
  })
_sym_db.RegisterMessage(AddResponse)

UpdatedFlight = _reflection.GeneratedProtocolMessageType('UpdatedFlight', (_message.Message,), {
  'DESCRIPTOR' : _UPDATEDFLIGHT,
  '__module__' : 'proto.Managment_pb2'
  # @@protoc_insertion_point(class_scope:proto.UpdatedFlight)
  })
_sym_db.RegisterMessage(UpdatedFlight)

ModFlightResponse = _reflection.GeneratedProtocolMessageType('ModFlightResponse', (_message.Message,), {
  'DESCRIPTOR' : _MODFLIGHTRESPONSE,
  '__module__' : 'proto.Managment_pb2'
  # @@protoc_insertion_point(class_scope:proto.ModFlightResponse)
  })
_sym_db.RegisterMessage(ModFlightResponse)

UpdatedSeats = _reflection.GeneratedProtocolMessageType('UpdatedSeats', (_message.Message,), {
  'DESCRIPTOR' : _UPDATEDSEATS,
  '__module__' : 'proto.Managment_pb2'
  # @@protoc_insertion_point(class_scope:proto.UpdatedSeats)
  })
_sym_db.RegisterMessage(UpdatedSeats)

ModSeatsResponse = _reflection.GeneratedProtocolMessageType('ModSeatsResponse', (_message.Message,), {
  'DESCRIPTOR' : _MODSEATSRESPONSE,
  '__module__' : 'proto.Managment_pb2'
  # @@protoc_insertion_point(class_scope:proto.ModSeatsResponse)
  })
_sym_db.RegisterMessage(ModSeatsResponse)

UpdatedServices = _reflection.GeneratedProtocolMessageType('UpdatedServices', (_message.Message,), {
  'DESCRIPTOR' : _UPDATEDSERVICES,
  '__module__' : 'proto.Managment_pb2'
  # @@protoc_insertion_point(class_scope:proto.UpdatedServices)
  })
_sym_db.RegisterMessage(UpdatedServices)

ModServicesResponse = _reflection.GeneratedProtocolMessageType('ModServicesResponse', (_message.Message,), {
  'DESCRIPTOR' : _MODSERVICESRESPONSE,
  '__module__' : 'proto.Managment_pb2'
  # @@protoc_insertion_point(class_scope:proto.ModServicesResponse)
  })
_sym_db.RegisterMessage(ModServicesResponse)

GetLogFileRequestMan = _reflection.GeneratedProtocolMessageType('GetLogFileRequestMan', (_message.Message,), {
  'DESCRIPTOR' : _GETLOGFILEREQUESTMAN,
  '__module__' : 'proto.Managment_pb2'
  # @@protoc_insertion_point(class_scope:proto.GetLogFileRequestMan)
  })
_sym_db.RegisterMessage(GetLogFileRequestMan)

GetLogFileReplyMan = _reflection.GeneratedProtocolMessageType('GetLogFileReplyMan', (_message.Message,), {
  'DESCRIPTOR' : _GETLOGFILEREPLYMAN,
  '__module__' : 'proto.Managment_pb2'
  # @@protoc_insertion_point(class_scope:proto.GetLogFileReplyMan)
  })
_sym_db.RegisterMessage(GetLogFileReplyMan)

_FLIGHTSINFO = DESCRIPTOR.services_by_name['FlightsInfo']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _SEATCOSTREQUEST._serialized_start=32
  _SEATCOSTREQUEST._serialized_end=68
  _SEATCOSTREPLY._serialized_start=70
  _SEATCOSTREPLY._serialized_end=101
  _ADDITIONALSERVICECOSTREQUEST._serialized_start=103
  _ADDITIONALSERVICECOSTREQUEST._serialized_end=152
  _ADDITIONALSERVICECOSTREPLY._serialized_start=154
  _ADDITIONALSERVICECOSTREPLY._serialized_end=198
  _PRICEREQUEST._serialized_start=200
  _PRICEREQUEST._serialized_end=230
  _PRICEREPLY._serialized_start=232
  _PRICEREPLY._serialized_end=259
  _NEWFLIGHT._serialized_start=262
  _NEWFLIGHT._serialized_end=440
  _ADDRESPONSE._serialized_start=442
  _ADDRESPONSE._serialized_end=484
  _UPDATEDFLIGHT._serialized_start=486
  _UPDATEDFLIGHT._serialized_end=537
  _MODFLIGHTRESPONSE._serialized_start=539
  _MODFLIGHTRESPONSE._serialized_end=587
  _UPDATEDSEATS._serialized_start=589
  _UPDATEDSEATS._serialized_end=702
  _MODSEATSRESPONSE._serialized_start=704
  _MODSEATSRESPONSE._serialized_end=751
  _UPDATEDSERVICES._serialized_start=754
  _UPDATEDSERVICES._serialized_end=890
  _MODSERVICESRESPONSE._serialized_start=892
  _MODSERVICESRESPONSE._serialized_end=942
  _GETLOGFILEREQUESTMAN._serialized_start=944
  _GETLOGFILEREQUESTMAN._serialized_end=988
  _GETLOGFILEREPLYMAN._serialized_start=990
  _GETLOGFILEREPLYMAN._serialized_end=1049
  _FLIGHTSINFO._serialized_start=1052
  _FLIGHTSINFO._serialized_end=1621
# @@protoc_insertion_point(module_scope)
