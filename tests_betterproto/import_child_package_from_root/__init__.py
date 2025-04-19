# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: import_child_package_from_root.proto
# plugin: python-betterproto2
# This file has been @generated

__all__ = ("Test",)

from dataclasses import dataclass

import betterproto2

from ..message_pool import default_message_pool

betterproto2.check_compiler_version("0.4.0")


@dataclass(eq=False, repr=False)
class Test(betterproto2.Message):
    """
    Tests generated imports when a message in root refers to a message in a child package.
    """

    child: "childpackage.Message | None" = betterproto2.field(1, betterproto2.TYPE_MESSAGE, optional=True)


default_message_pool.register_message("import_child_package_from_root", "Test", Test)


from . import childpackage
