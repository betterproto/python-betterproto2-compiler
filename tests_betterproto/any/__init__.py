# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: any.proto
# plugin: python-betterproto2
# This file has been @generated

__all__ = ("Person",)

from dataclasses import dataclass

import betterproto2

from ..message_pool import default_message_pool

betterproto2.check_compiler_version("0.4.0")


@dataclass(eq=False, repr=False)
class Person(betterproto2.Message):
    first_name: "str" = betterproto2.field(1, betterproto2.TYPE_STRING)

    last_name: "str" = betterproto2.field(2, betterproto2.TYPE_STRING)


default_message_pool.register_message("any", "Person", Person)
