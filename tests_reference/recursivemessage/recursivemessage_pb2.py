# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: recursivemessage.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x16recursivemessage.proto\x12\x10recursivemessage\"q\n\x04Test\x12\x0c\n\x04name\x18\x01 \x01(\t\x12%\n\x05\x63hild\x18\x02 \x01(\x0b\x32\x16.recursivemessage.Test\x12\x34\n\x0cintermediate\x18\x03 \x01(\x0b\x32\x1e.recursivemessage.Intermediate\"E\n\x0cIntermediate\x12\x0e\n\x06number\x18\x01 \x01(\x05\x12%\n\x05\x63hild\x18\x02 \x01(\x0b\x32\x16.recursivemessage.Testb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'recursivemessage_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_TEST']._serialized_start=44
  _globals['_TEST']._serialized_end=157
  _globals['_INTERMEDIATE']._serialized_start=159
  _globals['_INTERMEDIATE']._serialized_end=228
# @@protoc_insertion_point(module_scope)