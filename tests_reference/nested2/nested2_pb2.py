# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: nested2.proto
# Protobuf Python Version: 5.29.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    29,
    0,
    '',
    'nested2.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import package_pb2 as package__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\rnested2.proto\x12\x07nested2\x1a\rpackage.proto\",\n\x04Game\x1a$\n\x06Player\"\x1a\n\x04Race\x12\t\n\x05human\x10\x00\x12\x07\n\x03orc\x10\x01\"\xab\x01\n\x04Test\x12\x1b\n\x04game\x18\x01 \x01(\x0b\x32\r.nested2.Game\x12(\n\nGamePlayer\x18\x02 \x01(\x0b\x32\x14.nested2.Game.Player\x12\x31\n\x0eGamePlayerRace\x18\x03 \x01(\x0e\x32\x19.nested2.Game.Player.Race\x12)\n\x06Weapon\x18\x04 \x01(\x0b\x32\x19.nested2.equipment.Weaponb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'nested2_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_GAME']._serialized_start=41
  _globals['_GAME']._serialized_end=85
  _globals['_GAME_PLAYER']._serialized_start=49
  _globals['_GAME_PLAYER']._serialized_end=85
  _globals['_GAME_PLAYER_RACE']._serialized_start=59
  _globals['_GAME_PLAYER_RACE']._serialized_end=85
  _globals['_TEST']._serialized_start=88
  _globals['_TEST']._serialized_end=259
# @@protoc_insertion_point(module_scope)
