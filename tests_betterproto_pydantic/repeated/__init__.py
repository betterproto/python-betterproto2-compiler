# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: repeated.proto
# plugin: python-betterproto2
# This file has been @generated

__all__ = ("Test",)


import betterproto2
from pydantic.dataclasses import dataclass

from ..message_pool import default_message_pool

betterproto2.check_compiler_version("0.4.0")


@dataclass(eq=False, repr=False, config={"extra": "forbid"})
class Test(betterproto2.Message):
    names: "list[str]" = betterproto2.field(1, betterproto2.TYPE_STRING, repeated=True)


default_message_pool.register_message("repeated", "Test", Test)
