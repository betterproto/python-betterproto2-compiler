# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: pickling.proto
# plugin: python-betterproto2
# This file has been @generated

__all__ = (
    "Complex",
    "Fe",
    "Fi",
    "Fo",
    "NestedData",
    "PickledMessage",
    "Test",
)

from dataclasses import dataclass

import betterproto2

from ..message_pool import default_message_pool

betterproto2.check_compiler_version("0.2.4")


@dataclass(eq=False, repr=False)
class Complex(betterproto2.Message):
    """


    Oneofs:
        - grp:
    """

    foo_str: "str" = betterproto2.field(1, betterproto2.TYPE_STRING)

    fe: "Fe | None" = betterproto2.field(3, betterproto2.TYPE_MESSAGE, optional=True, group="grp")

    fi: "Fi | None" = betterproto2.field(4, betterproto2.TYPE_MESSAGE, optional=True, group="grp")

    fo: "Fo | None" = betterproto2.field(5, betterproto2.TYPE_MESSAGE, optional=True, group="grp")

    nested_data: "NestedData | None" = betterproto2.field(6, betterproto2.TYPE_MESSAGE, optional=True)

    mapping: "dict[str, _google__protobuf__.Any]" = betterproto2.field(
        7, betterproto2.TYPE_MAP, map_types=(betterproto2.TYPE_STRING, betterproto2.TYPE_MESSAGE)
    )


default_message_pool.register_message("pickling", "Complex", Complex)


@dataclass(eq=False, repr=False)
class Fe(betterproto2.Message):
    abc: "str" = betterproto2.field(1, betterproto2.TYPE_STRING)


default_message_pool.register_message("pickling", "Fe", Fe)


@dataclass(eq=False, repr=False)
class Fi(betterproto2.Message):
    abc: "str" = betterproto2.field(1, betterproto2.TYPE_STRING)


default_message_pool.register_message("pickling", "Fi", Fi)


@dataclass(eq=False, repr=False)
class Fo(betterproto2.Message):
    abc: "str" = betterproto2.field(1, betterproto2.TYPE_STRING)


default_message_pool.register_message("pickling", "Fo", Fo)


@dataclass(eq=False, repr=False)
class NestedData(betterproto2.Message):
    struct_foo: "dict[str, _google__protobuf__.Struct]" = betterproto2.field(
        1, betterproto2.TYPE_MAP, map_types=(betterproto2.TYPE_STRING, betterproto2.TYPE_MESSAGE)
    )

    map_str_any_bar: "dict[str, _google__protobuf__.Any]" = betterproto2.field(
        2, betterproto2.TYPE_MAP, map_types=(betterproto2.TYPE_STRING, betterproto2.TYPE_MESSAGE)
    )


default_message_pool.register_message("pickling", "NestedData", NestedData)


@dataclass(eq=False, repr=False)
class PickledMessage(betterproto2.Message):
    foo: "bool" = betterproto2.field(1, betterproto2.TYPE_BOOL)

    bar: "int" = betterproto2.field(2, betterproto2.TYPE_INT32)

    baz: "list[str]" = betterproto2.field(3, betterproto2.TYPE_STRING, repeated=True)


default_message_pool.register_message("pickling", "PickledMessage", PickledMessage)


@dataclass(eq=False, repr=False)
class Test(betterproto2.Message):
    pass


default_message_pool.register_message("pickling", "Test", Test)


from ..google import protobuf as _google__protobuf__