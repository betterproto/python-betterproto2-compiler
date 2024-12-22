# Getting started

## Install protoc

The betterproto2 compiler is a plugin of `protoc`, you first need to [install](https://grpc.io/docs/protoc-installation/) it.

## Install `betterproto2_compiler`

It is possible to install `betterproto2_compiler` using pip:

```
pip install betterproto2_compiler
```

## Compile a proto file

Create the following `example.proto` file.

```proto
syntax = "proto3";

package helloworld;

message HelloWorld {
    string message = 1;
}
```

You should now be able to compile it using:

```
mkdir lib
protoc -I . --python_betterproto2_out=lib example.proto
```
