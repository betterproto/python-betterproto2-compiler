# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: other.proto
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
    'other.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import root_pb2 as root__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0bother.proto\x12 import_circular_dependency.other\x1a\nroot.proto\"a\n\x13OtherPackageMessage\x12J\n\x12rootPackageMessage\x18\x01 \x01(\x0b\x32..import_circular_dependency.RootPackageMessageb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'other_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_OTHERPACKAGEMESSAGE']._serialized_start=61
  _globals['_OTHERPACKAGEMESSAGE']._serialized_end=158
# @@protoc_insertion_point(module_scope)
