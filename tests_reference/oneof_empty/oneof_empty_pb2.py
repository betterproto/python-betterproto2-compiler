# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: oneof_empty.proto
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
    'oneof_empty.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x11oneof_empty.proto\x12\x0boneof_empty\"\t\n\x07Nothing\"!\n\x0cMaybeNothing\x12\x11\n\tsometimes\x18* \x01(\t\"\x92\x01\n\x04Test\x12\'\n\x07nothing\x18\x01 \x01(\x0b\x32\x14.oneof_empty.NothingH\x00\x12+\n\x06maybe1\x18\x02 \x01(\x0b\x32\x19.oneof_empty.MaybeNothingH\x00\x12+\n\x06maybe2\x18\x03 \x01(\x0b\x32\x19.oneof_empty.MaybeNothingH\x00\x42\x07\n\x05\x65mptyb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'oneof_empty_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_NOTHING']._serialized_start=34
  _globals['_NOTHING']._serialized_end=43
  _globals['_MAYBENOTHING']._serialized_start=45
  _globals['_MAYBENOTHING']._serialized_end=78
  _globals['_TEST']._serialized_start=81
  _globals['_TEST']._serialized_end=227
# @@protoc_insertion_point(module_scope)
