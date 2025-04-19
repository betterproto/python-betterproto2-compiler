# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: test.proto
# plugin: python-betterproto2
# This file has been @generated

__all__ = ("Test",)

from dataclasses import dataclass

import betterproto2

from ....message_pool import default_message_pool

betterproto2.check_compiler_version("0.4.0")


@dataclass(eq=False, repr=False)
class Test(betterproto2.Message):
    """
    Verify that we can import a message unrelated to us, in a subpackage with the same name as us.
    """

    message: "__cousin__subpackage__.CousinMessage | None" = betterproto2.field(
        1, betterproto2.TYPE_MESSAGE, optional=True
    )


default_message_pool.register_message("import_cousin_package_same_name.test.subpackage", "Test", Test)


from ...cousin import subpackage as __cousin__subpackage__
