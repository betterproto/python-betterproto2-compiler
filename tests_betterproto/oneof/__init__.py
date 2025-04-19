# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: oneof.proto
# plugin: python-betterproto2
# This file has been @generated

__all__ = (
    "MixedDrink",
    "Test",
)

from dataclasses import dataclass

import betterproto2

from ..message_pool import default_message_pool

betterproto2.check_compiler_version("0.4.0")


@dataclass(eq=False, repr=False)
class MixedDrink(betterproto2.Message):
    shots: "int" = betterproto2.field(1, betterproto2.TYPE_INT32)


default_message_pool.register_message("oneof", "MixedDrink", MixedDrink)


@dataclass(eq=False, repr=False)
class Test(betterproto2.Message):
    """


    Oneofs:
        - foo:
        - bar:
    """

    pitied: "int | None" = betterproto2.field(1, betterproto2.TYPE_INT32, optional=True, group="foo")

    pitier: "str | None" = betterproto2.field(2, betterproto2.TYPE_STRING, optional=True, group="foo")

    just_a_regular_field: "int" = betterproto2.field(3, betterproto2.TYPE_INT32)

    drinks: "int | None" = betterproto2.field(11, betterproto2.TYPE_INT32, optional=True, group="bar")

    bar_name: "str | None" = betterproto2.field(12, betterproto2.TYPE_STRING, optional=True, group="bar")

    mixed_drink: "MixedDrink | None" = betterproto2.field(13, betterproto2.TYPE_MESSAGE, optional=True, group="bar")


default_message_pool.register_message("oneof", "Test", Test)
