# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: cousin.proto
# plugin: python-betterproto2
# This file has been @generated

__all__ = ("CousinMessage",)


import betterproto2
from pydantic.dataclasses import dataclass

from ....message_pool import default_message_pool

betterproto2.check_compiler_version("0.4.0")


@dataclass(eq=False, repr=False, config={"extra": "forbid"})
class CousinMessage(betterproto2.Message):
    pass


default_message_pool.register_message(
    "import_cousin_package_same_name.cousin.subpackage", "CousinMessage", CousinMessage
)
