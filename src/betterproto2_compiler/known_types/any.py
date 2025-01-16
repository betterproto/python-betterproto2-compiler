import betterproto2

from betterproto2_compiler.lib.google.protobuf import Any as VanillaAny

default_message_pool = betterproto2.MessagePool()  # Only for typing purpose


class Any(VanillaAny):
    def pack(self, message: betterproto2.Message, message_pool: "betterproto2.MessagePool | None" = None) -> None:
        """
        Pack the given message in the `Any` object.

        The message type must be registered in the message pool, which is done automatically when the module defining
        the message type is imported.
        """
        message_pool = message_pool or default_message_pool

        self.type_url = message_pool.type_to_url[type(message)]
        self.value = bytes(message)

    def unpack(self, message_pool: "betterproto2.MessagePool | None" = None) -> betterproto2.Message:
        """
        Return the message packed inside the `Any` object.

        The target message type must be registered in the message pool, which is done automatically when the module
        defining the message type is imported.
        """
        message_pool = message_pool or default_message_pool

        message_type = message_pool.url_to_type[self.type_url]

        return message_type().parse(self.value)

    def to_dict(self) -> dict:  # pyright: ignore [reportIncompatibleMethodOverride]
        # TOOO improve when dict is updated
        return {"@type": self.type_url, "value": self.unpack().to_dict()}
