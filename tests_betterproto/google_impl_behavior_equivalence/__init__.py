# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: google_impl_behavior_equivalence.proto
# plugin: python-betterproto2
# This file has been @generated

__all__ = (
    "Empty",
    "Foo",
    "Request",
    "Spam",
    "Test",
)

import datetime
from dataclasses import dataclass

import betterproto2

from ..message_pool import default_message_pool

betterproto2.check_compiler_version("0.4.0")


@dataclass(eq=False, repr=False)
class Empty(betterproto2.Message):
    pass


default_message_pool.register_message("google_impl_behavior_equivalence", "Empty", Empty)


@dataclass(eq=False, repr=False)
class Foo(betterproto2.Message):
    bar: "int" = betterproto2.field(1, betterproto2.TYPE_INT64)


default_message_pool.register_message("google_impl_behavior_equivalence", "Foo", Foo)


@dataclass(eq=False, repr=False)
class Request(betterproto2.Message):
    foo: "Empty | None" = betterproto2.field(1, betterproto2.TYPE_MESSAGE, optional=True)


default_message_pool.register_message("google_impl_behavior_equivalence", "Request", Request)


@dataclass(eq=False, repr=False)
class Spam(betterproto2.Message):
    ts: "datetime.datetime | None" = betterproto2.field(
        1, betterproto2.TYPE_MESSAGE, unwrap=lambda: _google__protobuf__.Timestamp, optional=True
    )


default_message_pool.register_message("google_impl_behavior_equivalence", "Spam", Spam)


@dataclass(eq=False, repr=False)
class Test(betterproto2.Message):
    """


    Oneofs:
        - group:
    """

    string: "str | None" = betterproto2.field(1, betterproto2.TYPE_STRING, optional=True, group="group")

    integer: "int | None" = betterproto2.field(2, betterproto2.TYPE_INT64, optional=True, group="group")

    foo: "Foo | None" = betterproto2.field(3, betterproto2.TYPE_MESSAGE, optional=True, group="group")


default_message_pool.register_message("google_impl_behavior_equivalence", "Test", Test)


from ..google import protobuf as _google__protobuf__
