from typing import TYPE_CHECKING

from betterproto2_compiler.lib.google.protobuf import (
    BoolValue as VanillaBoolValue,
    StringValue as VanillaStringValue,
)

if TYPE_CHECKING:
    from typing import Self


class BoolValue(VanillaBoolValue):
    @staticmethod
    def from_wrapped(wrapped: bool) -> "Self":
        return BoolValue(value=wrapped)

    def to_wrapped(self) -> bool:
        return self.value


class StringValue(VanillaStringValue):
    @staticmethod
    def from_wrapped(wrapped: str) -> "Self":
        return StringValue(value=wrapped)

    def to_wrapped(self) -> str:
        return self.value
