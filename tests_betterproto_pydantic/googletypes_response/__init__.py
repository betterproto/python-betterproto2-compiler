# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: googletypes_response.proto
# plugin: python-betterproto2
# This file has been @generated

__all__ = (
    "Input",
    "TestStub",
    "TestBase",
)

from typing import TYPE_CHECKING

import betterproto2
import grpclib
from betterproto2.grpc.grpclib_server import ServiceBase
from pydantic.dataclasses import dataclass

from ..message_pool import default_message_pool

if TYPE_CHECKING:
    import grpclib.server
    from betterproto2.grpc.grpclib_client import MetadataLike
    from grpclib.metadata import Deadline

betterproto2.check_compiler_version("0.2.4")


@dataclass(eq=False, repr=False, config={"extra": "forbid"})
class Input(betterproto2.Message):
    pass


default_message_pool.register_message("googletypes_response", "Input", Input)


class TestStub(betterproto2.ServiceStub):
    """
    Tests that wrapped values can be used directly as return values
    """

    async def get_double(
        self,
        message: "Input | None" = None,
        *,
        timeout: "float | None" = None,
        deadline: "Deadline | None" = None,
        metadata: "MetadataLike | None" = None,
    ) -> "_google__protobuf__.DoubleValue":
        if message is None:
            message = Input()

        return await self._unary_unary(
            "/googletypes_response.Test/GetDouble",
            message,
            _google__protobuf__.DoubleValue,
            timeout=timeout,
            deadline=deadline,
            metadata=metadata,
        )

    async def get_float(
        self,
        message: "Input | None" = None,
        *,
        timeout: "float | None" = None,
        deadline: "Deadline | None" = None,
        metadata: "MetadataLike | None" = None,
    ) -> "_google__protobuf__.FloatValue":
        if message is None:
            message = Input()

        return await self._unary_unary(
            "/googletypes_response.Test/GetFloat",
            message,
            _google__protobuf__.FloatValue,
            timeout=timeout,
            deadline=deadline,
            metadata=metadata,
        )

    async def get_int_64(
        self,
        message: "Input | None" = None,
        *,
        timeout: "float | None" = None,
        deadline: "Deadline | None" = None,
        metadata: "MetadataLike | None" = None,
    ) -> "_google__protobuf__.Int64Value":
        if message is None:
            message = Input()

        return await self._unary_unary(
            "/googletypes_response.Test/GetInt64",
            message,
            _google__protobuf__.Int64Value,
            timeout=timeout,
            deadline=deadline,
            metadata=metadata,
        )

    async def get_u_int_64(
        self,
        message: "Input | None" = None,
        *,
        timeout: "float | None" = None,
        deadline: "Deadline | None" = None,
        metadata: "MetadataLike | None" = None,
    ) -> "_google__protobuf__.UInt64Value":
        if message is None:
            message = Input()

        return await self._unary_unary(
            "/googletypes_response.Test/GetUInt64",
            message,
            _google__protobuf__.UInt64Value,
            timeout=timeout,
            deadline=deadline,
            metadata=metadata,
        )

    async def get_int_32(
        self,
        message: "Input | None" = None,
        *,
        timeout: "float | None" = None,
        deadline: "Deadline | None" = None,
        metadata: "MetadataLike | None" = None,
    ) -> "_google__protobuf__.Int32Value":
        if message is None:
            message = Input()

        return await self._unary_unary(
            "/googletypes_response.Test/GetInt32",
            message,
            _google__protobuf__.Int32Value,
            timeout=timeout,
            deadline=deadline,
            metadata=metadata,
        )

    async def get_u_int_32(
        self,
        message: "Input | None" = None,
        *,
        timeout: "float | None" = None,
        deadline: "Deadline | None" = None,
        metadata: "MetadataLike | None" = None,
    ) -> "_google__protobuf__.UInt32Value":
        if message is None:
            message = Input()

        return await self._unary_unary(
            "/googletypes_response.Test/GetUInt32",
            message,
            _google__protobuf__.UInt32Value,
            timeout=timeout,
            deadline=deadline,
            metadata=metadata,
        )

    async def get_bool(
        self,
        message: "Input | None" = None,
        *,
        timeout: "float | None" = None,
        deadline: "Deadline | None" = None,
        metadata: "MetadataLike | None" = None,
    ) -> "_google__protobuf__.BoolValue":
        if message is None:
            message = Input()

        return await self._unary_unary(
            "/googletypes_response.Test/GetBool",
            message,
            _google__protobuf__.BoolValue,
            timeout=timeout,
            deadline=deadline,
            metadata=metadata,
        )

    async def get_string(
        self,
        message: "Input | None" = None,
        *,
        timeout: "float | None" = None,
        deadline: "Deadline | None" = None,
        metadata: "MetadataLike | None" = None,
    ) -> "_google__protobuf__.StringValue":
        if message is None:
            message = Input()

        return await self._unary_unary(
            "/googletypes_response.Test/GetString",
            message,
            _google__protobuf__.StringValue,
            timeout=timeout,
            deadline=deadline,
            metadata=metadata,
        )

    async def get_bytes(
        self,
        message: "Input | None" = None,
        *,
        timeout: "float | None" = None,
        deadline: "Deadline | None" = None,
        metadata: "MetadataLike | None" = None,
    ) -> "_google__protobuf__.BytesValue":
        if message is None:
            message = Input()

        return await self._unary_unary(
            "/googletypes_response.Test/GetBytes",
            message,
            _google__protobuf__.BytesValue,
            timeout=timeout,
            deadline=deadline,
            metadata=metadata,
        )


from ..google import protobuf as _google__protobuf__


class TestBase(ServiceBase):
    """
    Tests that wrapped values can be used directly as return values
    """

    async def get_double(self, message: "Input") -> "_google__protobuf__.DoubleValue":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def get_float(self, message: "Input") -> "_google__protobuf__.FloatValue":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def get_int_64(self, message: "Input") -> "_google__protobuf__.Int64Value":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def get_u_int_64(self, message: "Input") -> "_google__protobuf__.UInt64Value":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def get_int_32(self, message: "Input") -> "_google__protobuf__.Int32Value":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def get_u_int_32(self, message: "Input") -> "_google__protobuf__.UInt32Value":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def get_bool(self, message: "Input") -> "_google__protobuf__.BoolValue":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def get_string(self, message: "Input") -> "_google__protobuf__.StringValue":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def get_bytes(self, message: "Input") -> "_google__protobuf__.BytesValue":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def __rpc_get_double(self, stream: "grpclib.server.Stream[Input, _google__protobuf__.DoubleValue]") -> None:
        request = await stream.recv_message()
        response = await self.get_double(request)
        await stream.send_message(response)

    async def __rpc_get_float(self, stream: "grpclib.server.Stream[Input, _google__protobuf__.FloatValue]") -> None:
        request = await stream.recv_message()
        response = await self.get_float(request)
        await stream.send_message(response)

    async def __rpc_get_int_64(self, stream: "grpclib.server.Stream[Input, _google__protobuf__.Int64Value]") -> None:
        request = await stream.recv_message()
        response = await self.get_int_64(request)
        await stream.send_message(response)

    async def __rpc_get_u_int_64(self, stream: "grpclib.server.Stream[Input, _google__protobuf__.UInt64Value]") -> None:
        request = await stream.recv_message()
        response = await self.get_u_int_64(request)
        await stream.send_message(response)

    async def __rpc_get_int_32(self, stream: "grpclib.server.Stream[Input, _google__protobuf__.Int32Value]") -> None:
        request = await stream.recv_message()
        response = await self.get_int_32(request)
        await stream.send_message(response)

    async def __rpc_get_u_int_32(self, stream: "grpclib.server.Stream[Input, _google__protobuf__.UInt32Value]") -> None:
        request = await stream.recv_message()
        response = await self.get_u_int_32(request)
        await stream.send_message(response)

    async def __rpc_get_bool(self, stream: "grpclib.server.Stream[Input, _google__protobuf__.BoolValue]") -> None:
        request = await stream.recv_message()
        response = await self.get_bool(request)
        await stream.send_message(response)

    async def __rpc_get_string(self, stream: "grpclib.server.Stream[Input, _google__protobuf__.StringValue]") -> None:
        request = await stream.recv_message()
        response = await self.get_string(request)
        await stream.send_message(response)

    async def __rpc_get_bytes(self, stream: "grpclib.server.Stream[Input, _google__protobuf__.BytesValue]") -> None:
        request = await stream.recv_message()
        response = await self.get_bytes(request)
        await stream.send_message(response)

    def __mapping__(self) -> "dict[str, grpclib.const.Handler":
        return {
            "/googletypes_response.Test/GetDouble": grpclib.const.Handler(
                self.__rpc_get_double,
                grpclib.const.Cardinality.UNARY_UNARY,
                Input,
                _google__protobuf__.DoubleValue,
            ),
            "/googletypes_response.Test/GetFloat": grpclib.const.Handler(
                self.__rpc_get_float,
                grpclib.const.Cardinality.UNARY_UNARY,
                Input,
                _google__protobuf__.FloatValue,
            ),
            "/googletypes_response.Test/GetInt64": grpclib.const.Handler(
                self.__rpc_get_int_64,
                grpclib.const.Cardinality.UNARY_UNARY,
                Input,
                _google__protobuf__.Int64Value,
            ),
            "/googletypes_response.Test/GetUInt64": grpclib.const.Handler(
                self.__rpc_get_u_int_64,
                grpclib.const.Cardinality.UNARY_UNARY,
                Input,
                _google__protobuf__.UInt64Value,
            ),
            "/googletypes_response.Test/GetInt32": grpclib.const.Handler(
                self.__rpc_get_int_32,
                grpclib.const.Cardinality.UNARY_UNARY,
                Input,
                _google__protobuf__.Int32Value,
            ),
            "/googletypes_response.Test/GetUInt32": grpclib.const.Handler(
                self.__rpc_get_u_int_32,
                grpclib.const.Cardinality.UNARY_UNARY,
                Input,
                _google__protobuf__.UInt32Value,
            ),
            "/googletypes_response.Test/GetBool": grpclib.const.Handler(
                self.__rpc_get_bool,
                grpclib.const.Cardinality.UNARY_UNARY,
                Input,
                _google__protobuf__.BoolValue,
            ),
            "/googletypes_response.Test/GetString": grpclib.const.Handler(
                self.__rpc_get_string,
                grpclib.const.Cardinality.UNARY_UNARY,
                Input,
                _google__protobuf__.StringValue,
            ),
            "/googletypes_response.Test/GetBytes": grpclib.const.Handler(
                self.__rpc_get_bytes,
                grpclib.const.Cardinality.UNARY_UNARY,
                Input,
                _google__protobuf__.BytesValue,
            ),
        }