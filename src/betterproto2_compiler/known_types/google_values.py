from betterproto2_compiler.lib.google.protobuf import (
    BoolValue as VanillaBoolValue,
    StringValue as VanillaStringValue,
)


class BoolValue(VanillaBoolValue):
    @staticmethod
    def from_wrapped(wrapped: bool) -> "BoolValue":
        return BoolValue(value=wrapped)

    def to_wrapped(self) -> bool:
        return self.value


class StringValue(VanillaStringValue):
    @staticmethod
    def from_wrapped(wrapped: str) -> "StringValue":
        return StringValue(value=wrapped)

    def to_wrapped(self) -> str:
        return self.value
