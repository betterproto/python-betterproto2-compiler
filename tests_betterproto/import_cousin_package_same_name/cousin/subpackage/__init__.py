# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: cousin.proto
# plugin: python-betterproto2
# This file has been @generated

__all__ = ("CousinMessage",)

from dataclasses import dataclass

import betterproto2

from ....message_pool import default_message_pool

betterproto2.check_compiler_version("0.2.4")


@dataclass(eq=False, repr=False)
class CousinMessage(betterproto2.Message):
    pass


default_message_pool.register_message(
    "import_cousin_package_same_name.cousin.subpackage", "CousinMessage", CousinMessage
)