# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: oneof_enum.proto
# plugin: python-betterproto2
# This file has been @generated

__all__ = (
    "Signal",
    "Move",
    "Test",
)

from dataclasses import dataclass

import betterproto2

from ..message_pool import default_message_pool

betterproto2.check_compiler_version("0.2.4")


class Signal(betterproto2.Enum):
    PASS = 0

    RESIGN = 1


@dataclass(eq=False, repr=False)
class Move(betterproto2.Message):
    x: "int" = betterproto2.field(1, betterproto2.TYPE_INT32)

    y: "int" = betterproto2.field(2, betterproto2.TYPE_INT32)


default_message_pool.register_message("oneof_enum", "Move", Move)


@dataclass(eq=False, repr=False)
class Test(betterproto2.Message):
    """


    Oneofs:
        - action:
    """

    signal: "Signal | None" = betterproto2.field(1, betterproto2.TYPE_ENUM, optional=True, group="action")

    move: "Move | None" = betterproto2.field(2, betterproto2.TYPE_MESSAGE, optional=True, group="action")


default_message_pool.register_message("oneof_enum", "Test", Test)