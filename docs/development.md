# Development

## Recompiling the lib proto files

After some updates in the compiler, it might be useful to recompile the standard Google proto files. As the proto files
are distributed with `protoc`, their path might depend on your installation.

```bash
mkdir lib
protoc \
    --python_betterproto2_opt=INCLUDE_GOOGLE \
    --python_betterproto2_out=lib \
    -I /usr/include/ \
    /usr/include/google/protobuf/*.proto
```

The generated files should be distributed in the `betterproto2` package.

!!! warning
    These proto files are written with the `proto2` syntax, which is not supported by betterproto. For the compiler to
    work, you need to manually patch the generated file to mark the field `oneof_index` in `Field` and
    `FieldDescriptorProto` optional.

In the compiler, you also need to compile the [plugin.proto](https://github.com/protocolbuffers/protobuf/blob/main/src/google/protobuf/compiler/plugin.proto)
file in `src/betterproto2_compiler/lib/google.protobug/compiler/__init__.py`.