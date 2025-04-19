# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: googletypes.proto
# plugin: python-betterproto2
# This file has been @generated

__all__ = ("Test",)

import datetime

import betterproto2
from pydantic.dataclasses import dataclass

from ..message_pool import default_message_pool

betterproto2.check_compiler_version("0.4.0")


@dataclass(eq=False, repr=False, config={"extra": "forbid"})
class Test(betterproto2.Message):
    maybe: "bool | None" = betterproto2.field(
        1, betterproto2.TYPE_MESSAGE, unwrap=lambda: _google__protobuf__.BoolValue, optional=True
    )

    ts: "datetime.datetime | None" = betterproto2.field(
        2, betterproto2.TYPE_MESSAGE, unwrap=lambda: _google__protobuf__.Timestamp, optional=True
    )

    duration: "datetime.timedelta | None" = betterproto2.field(
        3, betterproto2.TYPE_MESSAGE, unwrap=lambda: _google__protobuf__.Duration, optional=True
    )

    important: "int | None" = betterproto2.field(
        4, betterproto2.TYPE_MESSAGE, unwrap=lambda: _google__protobuf__.Int32Value, optional=True
    )

    empty: "_google__protobuf__.Empty | None" = betterproto2.field(5, betterproto2.TYPE_MESSAGE, optional=True)


default_message_pool.register_message("googletypes", "Test", Test)


from ..google import protobuf as _google__protobuf__
