Home
====

Welcome to `betterproto2_compiler`'s documentation! This page will guide you through the
steps needed to install and use the betterproto2 compiler.


## Getting started

### Install protoc

The betterproto2 compiler is a plugin of `protoc`, you first need to [install](https://grpc.io/docs/protoc-installation/) it.

### Install `betterproto2_compiler`

It is possible to install `betterproto2_compiler` using pip:

```
pip install betterproto2_compiler
```

### Compile a proto file

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
./protoc -I . --python_betterproto_out=lib example.proto
```
