# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: service.proto
# plugin: python-betterproto2
# This file has been @generated

__all__ = (
    "ThingType",
    "DoThingRequest",
    "DoThingResponse",
    "GetThingRequest",
    "GetThingResponse",
    "TestStub",
    "TestBase",
)

from collections.abc import AsyncIterable, AsyncIterator, Iterable
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


class ThingType(betterproto2.Enum):
    UNKNOWN = 0

    LIVING = 1

    DEAD = 2

    @classmethod
    def __get_pydantic_core_schema__(cls, _source_type, _handler):
        from pydantic_core import core_schema

        return core_schema.int_schema(ge=0)


@dataclass(eq=False, repr=False, config={"extra": "forbid"})
class DoThingRequest(betterproto2.Message):
    name: "str" = betterproto2.field(1, betterproto2.TYPE_STRING)

    comments: "list[str]" = betterproto2.field(2, betterproto2.TYPE_STRING, repeated=True)

    type: "ThingType" = betterproto2.field(3, betterproto2.TYPE_ENUM, default_factory=lambda: ThingType.try_value(0))


default_message_pool.register_message("service", "DoThingRequest", DoThingRequest)


@dataclass(eq=False, repr=False, config={"extra": "forbid"})
class DoThingResponse(betterproto2.Message):
    names: "list[str]" = betterproto2.field(1, betterproto2.TYPE_STRING, repeated=True)


default_message_pool.register_message("service", "DoThingResponse", DoThingResponse)


@dataclass(eq=False, repr=False, config={"extra": "forbid"})
class GetThingRequest(betterproto2.Message):
    name: "str" = betterproto2.field(1, betterproto2.TYPE_STRING)


default_message_pool.register_message("service", "GetThingRequest", GetThingRequest)


@dataclass(eq=False, repr=False, config={"extra": "forbid"})
class GetThingResponse(betterproto2.Message):
    name: "str" = betterproto2.field(1, betterproto2.TYPE_STRING)

    version: "int" = betterproto2.field(2, betterproto2.TYPE_INT32)


default_message_pool.register_message("service", "GetThingResponse", GetThingResponse)


class TestStub(betterproto2.ServiceStub):
    async def do_thing(
        self,
        message: "DoThingRequest",
        *,
        timeout: "float | None" = None,
        deadline: "Deadline | None" = None,
        metadata: "MetadataLike | None" = None,
    ) -> "DoThingResponse":
        return await self._unary_unary(
            "/service.Test/DoThing",
            message,
            DoThingResponse,
            timeout=timeout,
            deadline=deadline,
            metadata=metadata,
        )

    async def do_many_things(
        self,
        messages: "AsyncIterable[DoThingRequest] | Iterable[DoThingRequest]",
        *,
        timeout: "float | None" = None,
        deadline: "Deadline | None" = None,
        metadata: "MetadataLike | None" = None,
    ) -> "DoThingResponse":
        return await self._stream_unary(
            "/service.Test/DoManyThings",
            messages,
            DoThingRequest,
            DoThingResponse,
            timeout=timeout,
            deadline=deadline,
            metadata=metadata,
        )

    async def get_thing_versions(
        self,
        message: "GetThingRequest",
        *,
        timeout: "float | None" = None,
        deadline: "Deadline | None" = None,
        metadata: "MetadataLike | None" = None,
    ) -> "AsyncIterator[GetThingResponse]":
        async for response in self._unary_stream(
            "/service.Test/GetThingVersions",
            message,
            GetThingResponse,
            timeout=timeout,
            deadline=deadline,
            metadata=metadata,
        ):
            yield response

    async def get_different_things(
        self,
        messages: "AsyncIterable[GetThingRequest] | Iterable[GetThingRequest]",
        *,
        timeout: "float | None" = None,
        deadline: "Deadline | None" = None,
        metadata: "MetadataLike | None" = None,
    ) -> "AsyncIterator[GetThingResponse]":
        async for response in self._stream_stream(
            "/service.Test/GetDifferentThings",
            messages,
            GetThingRequest,
            GetThingResponse,
            timeout=timeout,
            deadline=deadline,
            metadata=metadata,
        ):
            yield response


class TestBase(ServiceBase):
    async def do_thing(self, message: "DoThingRequest") -> "DoThingResponse":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def do_many_things(self, messages: "AsyncIterator[DoThingRequest]") -> "DoThingResponse":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def get_thing_versions(self, message: "GetThingRequest") -> "AsyncIterator[GetThingResponse]":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def get_different_things(
        self, messages: "AsyncIterator[GetThingRequest]"
    ) -> "AsyncIterator[GetThingResponse]":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def __rpc_do_thing(self, stream: "grpclib.server.Stream[DoThingRequest, DoThingResponse]") -> None:
        request = await stream.recv_message()
        response = await self.do_thing(request)
        await stream.send_message(response)

    async def __rpc_do_many_things(self, stream: "grpclib.server.Stream[DoThingRequest, DoThingResponse]") -> None:
        request = stream.__aiter__()
        response = await self.do_many_things(request)
        await stream.send_message(response)

    async def __rpc_get_thing_versions(
        self, stream: "grpclib.server.Stream[GetThingRequest, GetThingResponse]"
    ) -> None:
        request = await stream.recv_message()
        await self._call_rpc_handler_server_stream(
            self.get_thing_versions,
            stream,
            request,
        )

    async def __rpc_get_different_things(
        self, stream: "grpclib.server.Stream[GetThingRequest, GetThingResponse]"
    ) -> None:
        request = stream.__aiter__()
        await self._call_rpc_handler_server_stream(
            self.get_different_things,
            stream,
            request,
        )

    def __mapping__(self) -> "dict[str, grpclib.const.Handler":
        return {
            "/service.Test/DoThing": grpclib.const.Handler(
                self.__rpc_do_thing,
                grpclib.const.Cardinality.UNARY_UNARY,
                DoThingRequest,
                DoThingResponse,
            ),
            "/service.Test/DoManyThings": grpclib.const.Handler(
                self.__rpc_do_many_things,
                grpclib.const.Cardinality.STREAM_UNARY,
                DoThingRequest,
                DoThingResponse,
            ),
            "/service.Test/GetThingVersions": grpclib.const.Handler(
                self.__rpc_get_thing_versions,
                grpclib.const.Cardinality.UNARY_STREAM,
                GetThingRequest,
                GetThingResponse,
            ),
            "/service.Test/GetDifferentThings": grpclib.const.Handler(
                self.__rpc_get_different_things,
                grpclib.const.Cardinality.STREAM_STREAM,
                GetThingRequest,
                GetThingResponse,
            ),
        }