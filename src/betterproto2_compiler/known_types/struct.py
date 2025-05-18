import typing

import betterproto2

from betterproto2_compiler.lib.google.protobuf import (
    ListValue as VanillaListValue,
    NullValue,
    Struct as VanillaStruct,
    Value as VanillaValue,
)


class Struct(VanillaStruct):
    # TODO typing
    def to_dict(
        self,
        *,
        output_format: betterproto2.OutputFormat = betterproto2.OutputFormat.PROTO_JSON,
        casing: betterproto2.Casing = betterproto2.Casing.CAMEL,
        include_default_values: bool = False,
    ) -> dict[str, typing.Any] | typing.Any:
        # If the output format is PYTHON, we should have kept the wraped type without building the real class
        assert output_format == betterproto2.OutputFormat.PROTO_JSON

        json = {}
        for name, value in self.fields.items():
            json[name] = value.to_dict()
        return json


class Value(VanillaValue):
    def to_dict(
        self,
        *,
        output_format: betterproto2.OutputFormat = betterproto2.OutputFormat.PROTO_JSON,
        casing: betterproto2.Casing = betterproto2.Casing.CAMEL,
        include_default_values: bool = False,
    ) -> dict[str, typing.Any] | typing.Any:
        # If the output format is PYTHON, we should have kept the wraped type without building the real class
        assert output_format == betterproto2.OutputFormat.PROTO_JSON

        match self:
            case Value(null_value=NullValue()):
                return None
            case Value(number_value=float(number_value)):
                return number_value
            case Value(string_value=str(string_value)):
                return string_value
            case Value(bool_value=bool(bool_value)):
                return bool_value
            case Value(struct_value=struct_value) if struct_value is not None:
                return struct_value.to_dict()
            case Value(list_value=list_value) if list_value is not None:
                return list_value.to_dict()


class ListValue(VanillaListValue):
    def to_dict(
        self,
        *,
        output_format: betterproto2.OutputFormat = betterproto2.OutputFormat.PROTO_JSON,
        casing: betterproto2.Casing = betterproto2.Casing.CAMEL,
        include_default_values: bool = False,
    ) -> dict[str, typing.Any] | typing.Any:
        # If the output format is PYTHON, we should have kept the wraped type without building the real class
        assert output_format == betterproto2.OutputFormat.PROTO_JSON

        json = []
        for value in self.values:
            json.append(value.to_dict())
        return json
