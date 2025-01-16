from collections.abc import Callable

from .any import Any
from .duration import Duration
from .timestamp import Timestamp

# For each (package, message name), lists the methods that should be added to the message definition.
# The source code of the method is read from the `known_types` folder. If imports are needed, they can be directly added
# to the template file: they will automatically be removed if not necessary.
KNOWN_METHODS: dict[tuple[str, str], list[Callable]] = {
    ("google.protobuf", "Any"): [Any.pack, Any.unpack, Any.to_dict],
    ("google.protobuf", "Timestamp"): [Timestamp.from_datetime, Timestamp.to_datetime, Timestamp.timestamp_to_json],
    ("google.protobuf", "Duration"): [Duration.from_timedelta, Duration.to_timedelta, Duration.delta_to_json],
}
