import datetime

from betterproto2_compiler.lib.google.protobuf import Timestamp as VanillaTimestamp


class Timestamp(VanillaTimestamp):
    @classmethod
    def from_datetime(cls, dt: datetime.datetime) -> "Timestamp":
        # manual epoch offset calulation to avoid rounding errors,
        # to support negative timestamps (before 1970) and skirt
        # around datetime bugs (apparently 0 isn't a year in [0, 9999]??)
        offset = dt - datetime.datetime(1970, 1, 1, tzinfo=datetime.timezone.utc)
        # below is the same as timedelta.total_seconds() but without dividing by 1e6
        # so we end up with microseconds as integers instead of seconds as float
        offset_us = (offset.days * 24 * 60 * 60 + offset.seconds) * 10**6 + offset.microseconds
        seconds, us = divmod(offset_us, 10**6)
        return cls(seconds, us * 1000)

    def to_datetime(self) -> datetime.datetime:
        # datetime.fromtimestamp() expects a timestamp in seconds, not microseconds
        # if we pass it as a floating point number, we will run into rounding errors
        # see also #407
        offset = datetime.timedelta(seconds=self.seconds, microseconds=self.nanos // 1000)
        return datetime.datetime(1970, 1, 1, tzinfo=datetime.timezone.utc) + offset

    @staticmethod
    def timestamp_to_json(dt: datetime.datetime) -> str:
        nanos = dt.microsecond * 1e3
        if dt.tzinfo is not None:
            # change timezone aware datetime objects to utc
            dt = dt.astimezone(datetime.timezone.utc)
        copy = dt.replace(microsecond=0, tzinfo=None)
        result = copy.isoformat()
        if (nanos % 1e9) == 0:
            # If there are 0 fractional digits, the fractional
            # point '.' should be omitted when serializing.
            return f"{result}Z"
        if (nanos % 1e6) == 0:
            # Serialize 3 fractional digits.
            return f"{result}.{int(nanos // 1e6) :03d}Z"
        if (nanos % 1e3) == 0:
            # Serialize 6 fractional digits.
            return f"{result}.{int(nanos // 1e3) :06d}Z"
        # Serialize 9 fractional digits.
        return f"{result}.{nanos:09d}"
