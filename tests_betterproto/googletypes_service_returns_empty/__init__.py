# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: googletypes_service_returns_empty.proto
# plugin: python-betterproto2
# This file has been @generated

__all__ = (
    "RequestMessage",
    "TestStub",
    "TestBase",
)

from dataclasses import dataclass
from typing import TYPE_CHECKING

import betterproto2
import grpclib
from betterproto2.grpc.grpclib_server import ServiceBase

from ..message_pool import default_message_pool

if TYPE_CHECKING:
    import grpclib.server
    from betterproto2.grpc.grpclib_client import MetadataLike
    from grpclib.metadata import Deadline

betterproto2.check_compiler_version("0.2.4")


@dataclass(eq=False, repr=False)
class RequestMessage(betterproto2.Message):
    pass


default_message_pool.register_message("googletypes_service_returns_empty", "RequestMessage", RequestMessage)


class TestStub(betterproto2.ServiceStub):
    async def send(
        self,
        message: "RequestMessage | None" = None,
        *,
        timeout: "float | None" = None,
        deadline: "Deadline | None" = None,
        metadata: "MetadataLike | None" = None,
    ) -> "_google__protobuf__.Empty":
        if message is None:
            message = RequestMessage()

        return await self._unary_unary(
            "/googletypes_service_returns_empty.Test/Send",
            message,
            _google__protobuf__.Empty,
            timeout=timeout,
            deadline=deadline,
            metadata=metadata,
        )


from ..google import protobuf as _google__protobuf__


class TestBase(ServiceBase):
    async def send(self, message: "RequestMessage") -> "_google__protobuf__.Empty":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def __rpc_send(self, stream: "grpclib.server.Stream[RequestMessage, _google__protobuf__.Empty]") -> None:
        request = await stream.recv_message()
        response = await self.send(request)
        await stream.send_message(response)

    def __mapping__(self) -> "dict[str, grpclib.const.Handler":
        return {
            "/googletypes_service_returns_empty.Test/Send": grpclib.const.Handler(
                self.__rpc_send,
                grpclib.const.Cardinality.UNARY_UNARY,
                RequestMessage,
                _google__protobuf__.Empty,
            ),
        }