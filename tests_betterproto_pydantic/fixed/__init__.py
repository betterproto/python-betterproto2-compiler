# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: fixed.proto
# plugin: python-betterproto2
# This file has been @generated

__all__ = ("Test",)


import betterproto2
from pydantic.dataclasses import dataclass

from ..message_pool import default_message_pool

betterproto2.check_compiler_version("0.2.4")


@dataclass(eq=False, repr=False, config={"extra": "forbid"})
class Test(betterproto2.Message):
    foo: "int" = betterproto2.field(1, betterproto2.TYPE_FIXED32)

    bar: "int" = betterproto2.field(2, betterproto2.TYPE_SFIXED32)

    baz: "int" = betterproto2.field(3, betterproto2.TYPE_FIXED64)

    qux: "int" = betterproto2.field(4, betterproto2.TYPE_SFIXED64)


default_message_pool.register_message("fixed", "Test", Test)