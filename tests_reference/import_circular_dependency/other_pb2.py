# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: other.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import root_pb2 as root__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0bother.proto\x12 import_circular_dependency.other\x1a\nroot.proto\"a\n\x13OtherPackageMessage\x12J\n\x12rootPackageMessage\x18\x01 \x01(\x0b\x32..import_circular_dependency.RootPackageMessageb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'other_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_OTHERPACKAGEMESSAGE']._serialized_start=61
  _globals['_OTHERPACKAGEMESSAGE']._serialized_end=158
# @@protoc_insertion_point(module_scope)