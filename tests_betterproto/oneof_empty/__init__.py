# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: oneof_empty.proto
# plugin: python-betterproto2
# This file has been @generated

__all__ = (
    "MaybeNothing",
    "Nothing",
    "Test",
)

from dataclasses import dataclass

import betterproto2

from ..message_pool import default_message_pool

betterproto2.check_compiler_version("0.2.4")


@dataclass(eq=False, repr=False)
class MaybeNothing(betterproto2.Message):
    sometimes: "str" = betterproto2.field(42, betterproto2.TYPE_STRING)


default_message_pool.register_message("oneof_empty", "MaybeNothing", MaybeNothing)


@dataclass(eq=False, repr=False)
class Nothing(betterproto2.Message):
    pass


default_message_pool.register_message("oneof_empty", "Nothing", Nothing)


@dataclass(eq=False, repr=False)
class Test(betterproto2.Message):
    """


    Oneofs:
        - empty:
    """

    nothing: "Nothing | None" = betterproto2.field(1, betterproto2.TYPE_MESSAGE, optional=True, group="empty")

    maybe1: "MaybeNothing | None" = betterproto2.field(2, betterproto2.TYPE_MESSAGE, optional=True, group="empty")

    maybe2: "MaybeNothing | None" = betterproto2.field(3, betterproto2.TYPE_MESSAGE, optional=True, group="empty")


default_message_pool.register_message("oneof_empty", "Test", Test)