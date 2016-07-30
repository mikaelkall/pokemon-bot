# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: POGOProtos/Settings/GlobalSettings.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from POGOProtos.Settings import FortSettings_pb2 as POGOProtos_dot_Settings_dot_FortSettings__pb2
from POGOProtos.Settings import MapSettings_pb2 as POGOProtos_dot_Settings_dot_MapSettings__pb2
from POGOProtos.Settings import LevelSettings_pb2 as POGOProtos_dot_Settings_dot_LevelSettings__pb2
from POGOProtos.Settings import InventorySettings_pb2 as POGOProtos_dot_Settings_dot_InventorySettings__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='POGOProtos/Settings/GlobalSettings.proto',
  package='POGOProtos.Settings',
  syntax='proto3',
  serialized_pb=_b('\n(POGOProtos/Settings/GlobalSettings.proto\x12\x13POGOProtos.Settings\x1a&POGOProtos/Settings/FortSettings.proto\x1a%POGOProtos/Settings/MapSettings.proto\x1a\'POGOProtos/Settings/LevelSettings.proto\x1a+POGOProtos/Settings/InventorySettings.proto\"\xa2\x02\n\x0eGlobalSettings\x12\x38\n\rfort_settings\x18\x02 \x01(\x0b\x32!.POGOProtos.Settings.FortSettings\x12\x36\n\x0cmap_settings\x18\x03 \x01(\x0b\x32 .POGOProtos.Settings.MapSettings\x12:\n\x0elevel_settings\x18\x04 \x01(\x0b\x32\".POGOProtos.Settings.LevelSettings\x12\x42\n\x12inventory_settings\x18\x05 \x01(\x0b\x32&.POGOProtos.Settings.InventorySettings\x12\x1e\n\x16minimum_client_version\x18\x06 \x01(\tb\x06proto3')
  ,
  dependencies=[POGOProtos_dot_Settings_dot_FortSettings__pb2.DESCRIPTOR,POGOProtos_dot_Settings_dot_MapSettings__pb2.DESCRIPTOR,POGOProtos_dot_Settings_dot_LevelSettings__pb2.DESCRIPTOR,POGOProtos_dot_Settings_dot_InventorySettings__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_GLOBALSETTINGS = _descriptor.Descriptor(
  name='GlobalSettings',
  full_name='POGOProtos.Settings.GlobalSettings',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='fort_settings', full_name='POGOProtos.Settings.GlobalSettings.fort_settings', index=0,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='map_settings', full_name='POGOProtos.Settings.GlobalSettings.map_settings', index=1,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='level_settings', full_name='POGOProtos.Settings.GlobalSettings.level_settings', index=2,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='inventory_settings', full_name='POGOProtos.Settings.GlobalSettings.inventory_settings', index=3,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='minimum_client_version', full_name='POGOProtos.Settings.GlobalSettings.minimum_client_version', index=4,
      number=6, type=9, cpp_type=9, label=1,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=231,
  serialized_end=521,
)

_GLOBALSETTINGS.fields_by_name['fort_settings'].message_type = POGOProtos_dot_Settings_dot_FortSettings__pb2._FORTSETTINGS
_GLOBALSETTINGS.fields_by_name['map_settings'].message_type = POGOProtos_dot_Settings_dot_MapSettings__pb2._MAPSETTINGS
_GLOBALSETTINGS.fields_by_name['level_settings'].message_type = POGOProtos_dot_Settings_dot_LevelSettings__pb2._LEVELSETTINGS
_GLOBALSETTINGS.fields_by_name['inventory_settings'].message_type = POGOProtos_dot_Settings_dot_InventorySettings__pb2._INVENTORYSETTINGS
DESCRIPTOR.message_types_by_name['GlobalSettings'] = _GLOBALSETTINGS

GlobalSettings = _reflection.GeneratedProtocolMessageType('GlobalSettings', (_message.Message,), dict(
  DESCRIPTOR = _GLOBALSETTINGS,
  __module__ = 'POGOProtos.Settings.GlobalSettings_pb2'
  # @@protoc_insertion_point(class_scope:POGOProtos.Settings.GlobalSettings)
  ))
_sym_db.RegisterMessage(GlobalSettings)


# @@protoc_insertion_point(module_scope)
