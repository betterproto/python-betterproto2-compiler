import datetime

from betterproto2_compiler.lib.google.protobuf import Duration as VanillaDuration


class Duration(VanillaDuration):
    @classmethod
    def from_timedelta(
        cls, delta: datetime.timedelta, *, _1_microsecond: datetime.timedelta = datetime.timedelta(microseconds=1)
    ) -> "Duration":
        total_ms = delta // _1_microsecond
        seconds = int(total_ms / 1e6)
        nanos = int((total_ms % 1e6) * 1e3)
        return cls(seconds, nanos)

    def to_timedelta(self) -> datetime.timedelta:
        return datetime.timedelta(seconds=self.seconds, microseconds=self.nanos / 1e3)

    @staticmethod
    def delta_to_json(delta: datetime.timedelta) -> str:
        parts = str(delta.total_seconds()).split(".")
        if len(parts) > 1:
            while len(parts[1]) not in (3, 6, 9):
                parts[1] = f"{parts[1]}0"
        return f"{'.'.join(parts)}s"
