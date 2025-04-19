# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: googletypes_response_embedded.proto
# plugin: python-betterproto2
# This file has been @generated

__all__ = (
    "Input",
    "Output",
    "TestStub",
    "TestBase",
)

from typing import TYPE_CHECKING

import betterproto2
import grpc
import grpclib
from betterproto2.grpc.grpclib_server import ServiceBase
from pydantic.dataclasses import dataclass

from ..message_pool import default_message_pool

if TYPE_CHECKING:
    import grpclib.server
    from betterproto2.grpc.grpclib_client import MetadataLike
    from grpclib.metadata import Deadline

betterproto2.check_compiler_version("0.4.0")


@dataclass(eq=False, repr=False, config={"extra": "forbid"})
class Input(betterproto2.Message):
    pass


default_message_pool.register_message("googletypes_response_embedded", "Input", Input)


@dataclass(eq=False, repr=False, config={"extra": "forbid"})
class Output(betterproto2.Message):
    double_value: "float | None" = betterproto2.field(
        1, betterproto2.TYPE_MESSAGE, unwrap=lambda: _google__protobuf__.DoubleValue, optional=True
    )

    float_value: "float | None" = betterproto2.field(
        2, betterproto2.TYPE_MESSAGE, unwrap=lambda: _google__protobuf__.FloatValue, optional=True
    )

    int64_value: "int | None" = betterproto2.field(
        3, betterproto2.TYPE_MESSAGE, unwrap=lambda: _google__protobuf__.Int64Value, optional=True
    )

    uint64_value: "int | None" = betterproto2.field(
        4, betterproto2.TYPE_MESSAGE, unwrap=lambda: _google__protobuf__.UInt64Value, optional=True
    )

    int32_value: "int | None" = betterproto2.field(
        5, betterproto2.TYPE_MESSAGE, unwrap=lambda: _google__protobuf__.Int32Value, optional=True
    )

    uint32_value: "int | None" = betterproto2.field(
        6, betterproto2.TYPE_MESSAGE, unwrap=lambda: _google__protobuf__.UInt32Value, optional=True
    )

    bool_value: "bool | None" = betterproto2.field(
        7, betterproto2.TYPE_MESSAGE, unwrap=lambda: _google__protobuf__.BoolValue, optional=True
    )

    string_value: "str | None" = betterproto2.field(
        8, betterproto2.TYPE_MESSAGE, unwrap=lambda: _google__protobuf__.StringValue, optional=True
    )

    bytes_value: "bytes | None" = betterproto2.field(
        9, betterproto2.TYPE_MESSAGE, unwrap=lambda: _google__protobuf__.BytesValue, optional=True
    )


default_message_pool.register_message("googletypes_response_embedded", "Output", Output)


class TestSyncStub:
    """
    Tests that wrapped values are supported as part of output message
    """

    def __init__(self, channel: grpc.Channel):
        self._channel = channel

    def get_output(self, message: "Input | None" = None) -> "Output":
        if message is None:
            message = Input()

        return self._channel.unary_unary(
            "/googletypes_response_embedded.Test/getOutput",
            Input.SerializeToString,
            Output.FromString,
        )(message)


class TestStub(betterproto2.ServiceStub):
    """
    Tests that wrapped values are supported as part of output message
    """

    async def get_output(
        self,
        message: "Input | None" = None,
        *,
        timeout: "float | None" = None,
        deadline: "Deadline | None" = None,
        metadata: "MetadataLike | None" = None,
    ) -> "Output":
        if message is None:
            message = Input()

        return await self._unary_unary(
            "/googletypes_response_embedded.Test/getOutput",
            message,
            Output,
            timeout=timeout,
            deadline=deadline,
            metadata=metadata,
        )


from ..google import protobuf as _google__protobuf__


class TestBase(ServiceBase):
    """
    Tests that wrapped values are supported as part of output message
    """

    async def get_output(self, message: "Input") -> "Output":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def __rpc_get_output(self, stream: "grpclib.server.Stream[Input, Output]") -> None:
        request = await stream.recv_message()
        response = await self.get_output(request)
        await stream.send_message(response)

    def __mapping__(self) -> "dict[str, grpclib.const.Handler]":
        return {
            "/googletypes_response_embedded.Test/getOutput": grpclib.const.Handler(
                self.__rpc_get_output,
                grpclib.const.Cardinality.UNARY_UNARY,
                Input,
                Output,
            ),
        }
