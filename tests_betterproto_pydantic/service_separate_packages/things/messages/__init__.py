# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: messages.proto
# plugin: python-betterproto2
# This file has been @generated

__all__ = (
    "DoThingRequest",
    "DoThingResponse",
    "GetThingRequest",
    "GetThingResponse",
)

import datetime

import betterproto2
from pydantic.dataclasses import dataclass

from ....message_pool import default_message_pool

betterproto2.check_compiler_version("0.2.4")


@dataclass(eq=False, repr=False, config={"extra": "forbid"})
class DoThingRequest(betterproto2.Message):
    name: "str" = betterproto2.field(1, betterproto2.TYPE_STRING)

    comments: "list[str]" = betterproto2.field(2, betterproto2.TYPE_STRING, repeated=True)
    """
    use `repeated` so we can check if `List` is correctly imported
    """

    when: "datetime.datetime | None" = betterproto2.field(3, betterproto2.TYPE_MESSAGE, optional=True)
    """
    use google types `timestamp` and `duration` so we can check
    if everything from `datetime` is correctly imported
    """

    duration: "datetime.timedelta | None" = betterproto2.field(4, betterproto2.TYPE_MESSAGE, optional=True)


default_message_pool.register_message("service_separate_packages.things.messages", "DoThingRequest", DoThingRequest)


@dataclass(eq=False, repr=False, config={"extra": "forbid"})
class DoThingResponse(betterproto2.Message):
    names: "list[str]" = betterproto2.field(1, betterproto2.TYPE_STRING, repeated=True)


default_message_pool.register_message("service_separate_packages.things.messages", "DoThingResponse", DoThingResponse)


@dataclass(eq=False, repr=False, config={"extra": "forbid"})
class GetThingRequest(betterproto2.Message):
    name: "str" = betterproto2.field(1, betterproto2.TYPE_STRING)


default_message_pool.register_message("service_separate_packages.things.messages", "GetThingRequest", GetThingRequest)


@dataclass(eq=False, repr=False, config={"extra": "forbid"})
class GetThingResponse(betterproto2.Message):
    name: "str" = betterproto2.field(1, betterproto2.TYPE_STRING)

    version: "int" = betterproto2.field(2, betterproto2.TYPE_INT32)


default_message_pool.register_message("service_separate_packages.things.messages", "GetThingResponse", GetThingResponse)