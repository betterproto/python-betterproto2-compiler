# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: regression_387.proto
# plugin: python-betterproto2
# This file has been @generated

__all__ = (
    "ParentElement",
    "Test",
)


import betterproto2
from pydantic.dataclasses import dataclass

from ..message_pool import default_message_pool

betterproto2.check_compiler_version("0.4.0")


@dataclass(eq=False, repr=False, config={"extra": "forbid"})
class ParentElement(betterproto2.Message):
    name: "str" = betterproto2.field(1, betterproto2.TYPE_STRING)

    elems: "list[Test]" = betterproto2.field(2, betterproto2.TYPE_MESSAGE, repeated=True)


default_message_pool.register_message("regression_387", "ParentElement", ParentElement)


@dataclass(eq=False, repr=False, config={"extra": "forbid"})
class Test(betterproto2.Message):
    id: "int" = betterproto2.field(1, betterproto2.TYPE_UINT64)


default_message_pool.register_message("regression_387", "Test", Test)
