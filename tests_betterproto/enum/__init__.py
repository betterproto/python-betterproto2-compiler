# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: enum.proto
# plugin: python-betterproto2
# This file has been @generated

__all__ = (
    "ArithmeticOperator",
    "Choice",
    "Test",
)

from dataclasses import dataclass

import betterproto2

from ..message_pool import default_message_pool

betterproto2.check_compiler_version("0.2.4")


class ArithmeticOperator(betterproto2.Enum):
    """
    A "C" like enum with the enum name prefixed onto members, these should be stripped
    """

    NONE = 0

    PLUS = 1

    MINUS = 2

    _0_PREFIXED = 3


class Choice(betterproto2.Enum):
    ZERO = 0

    ONE = 1

    FOUR = 4
    """
    TWO = 2;
    """

    THREE = 3


@dataclass(eq=False, repr=False)
class Test(betterproto2.Message):
    """
    Tests that enums are correctly serialized and that it correctly handles skipped and out-of-order enum values
    """

    choice: "Choice" = betterproto2.field(1, betterproto2.TYPE_ENUM, default_factory=lambda: Choice.try_value(0))

    choices: "list[Choice]" = betterproto2.field(2, betterproto2.TYPE_ENUM, repeated=True)


default_message_pool.register_message("enum", "Test", Test)