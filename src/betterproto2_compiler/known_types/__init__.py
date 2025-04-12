from collections.abc import Callable

from .any import Any
from .duration import Duration
from .google_values import BoolValue, StringValue
from .timestamp import Timestamp

# For each (package, message name), lists the methods that should be added to the message definition.
# The source code of the method is read from the `known_types` folder. If imports are needed, they can be directly added
# to the template file: they will automatically be removed if not necessary.
KNOWN_METHODS: dict[tuple[str, str], list[Callable]] = {
    ("google.protobuf", "Any"): [Any.pack, Any.unpack, Any.to_dict],
    ("google.protobuf", "Timestamp"): [
        Timestamp.from_datetime,
        Timestamp.to_datetime,
        Timestamp.timestamp_to_json,
        Timestamp.from_dict,
        Timestamp.to_wrapped,
    ],
    ("google.protobuf", "Duration"): [Duration.from_timedelta, Duration.to_timedelta, Duration.delta_to_json],
    ("google.protobuf", "BoolValue"): [BoolValue.from_wrapped, BoolValue.to_wrapped],
    ("google.protobuf", "StringValue"): [StringValue.from_wrapped, StringValue.to_wrapped],
}

# A wrapped type is the type of a message that is automatically replaced by a known Python type.
WRAPPED_TYPES: dict[tuple[str, str], str] = {
    ("google.protobuf", "BoolValue"): "bool",
    ("google.protobuf", "StringValue"): "str",
    ("google.protobuf", "Timestamp"): "datetime.datetime",
    ("google.protobuf", "Duration"): "datetime.timedelta",
}
