# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: test.proto
# plugin: python-betterproto2
# This file has been @generated

__all__ = ("Test",)

from dataclasses import dataclass

import betterproto2

from ..message_pool import default_message_pool

betterproto2.check_compiler_version("0.2.4")


@dataclass(eq=False, repr=False)
class Test(betterproto2.Message):
    """
    Tests that we can import from a package with a capital name, that looks like a nested type, but isn't.
    """

    message: "Capitalized.Message | None" = betterproto2.field(1, betterproto2.TYPE_MESSAGE, optional=True)


default_message_pool.register_message("import_capitalized_package", "Test", Test)


from . import Capitalized