# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: POGOProtos/Data/DownloadUrlEntry.proto

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
  name='POGOProtos/Data/DownloadUrlEntry.proto',
  package='POGOProtos.Data',
  syntax='proto3',
  serialized_pb=_b('\n&POGOProtos/Data/DownloadUrlEntry.proto\x12\x0fPOGOProtos.Data\"Q\n\x10\x44ownloadUrlEntry\x12\x10\n\x08\x61sset_id\x18\x01 \x01(\t\x12\x0b\n\x03url\x18\x02 \x01(\t\x12\x0c\n\x04size\x18\x03 \x01(\x05\x12\x10\n\x08\x63hecksum\x18\x04 \x01(\rb\x06proto3')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_DOWNLOADURLENTRY = _descriptor.Descriptor(
  name='DownloadUrlEntry',
  full_name='POGOProtos.Data.DownloadUrlEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='asset_id', full_name='POGOProtos.Data.DownloadUrlEntry.asset_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='url', full_name='POGOProtos.Data.DownloadUrlEntry.url', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='size', full_name='POGOProtos.Data.DownloadUrlEntry.size', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='checksum', full_name='POGOProtos.Data.DownloadUrlEntry.checksum', index=3,
      number=4, type=13, cpp_type=3, label=1,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=59,
  serialized_end=140,
)

DESCRIPTOR.message_types_by_name['DownloadUrlEntry'] = _DOWNLOADURLENTRY

DownloadUrlEntry = _reflection.GeneratedProtocolMessageType('DownloadUrlEntry', (_message.Message,), dict(
  DESCRIPTOR = _DOWNLOADURLENTRY,
  __module__ = 'POGOProtos.Data.DownloadUrlEntry_pb2'
  # @@protoc_insertion_point(class_scope:POGOProtos.Data.DownloadUrlEntry)
  ))
_sym_db.RegisterMessage(DownloadUrlEntry)


# @@protoc_insertion_point(module_scope)
