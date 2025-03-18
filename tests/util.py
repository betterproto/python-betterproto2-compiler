import asyncio
import atexit
import os
import platform
import sys
import tempfile
from collections.abc import Generator
from pathlib import Path

os.environ["PROTOCOL_BUFFERS_PYTHON_IMPLEMENTATION"] = "python"

root_path = Path(__file__).resolve().parent
inputs_path = root_path.joinpath("inputs")
output_path_reference = root_path.joinpath("output_reference")
output_path_betterproto = root_path.joinpath("output_betterproto")
output_path_betterproto_pydantic = root_path.joinpath("output_betterproto_pydantic")


def get_files(path, suffix: str) -> Generator[str, None, None]:
    for r, dirs, files in os.walk(path):
        for filename in [f for f in files if f.endswith(suffix)]:
            yield os.path.join(r, filename)


def get_directories(path):
    for root, directories, files in os.walk(path):
        yield from directories


async def protoc(
    path: str | Path,
    output_dir: str | Path,
    reference: bool = False,
    pydantic_dataclasses: bool = False,
):
    path: Path = Path(path).resolve()
    output_dir: Path = Path(output_dir).resolve()
    python_out_option: str = "python_betterproto2_out" if not reference else "python_out"

    if pydantic_dataclasses:
        plugin_path = Path("src/betterproto2_compiler/plugin/main.py")

        if "Win" in platform.system():
            with tempfile.NamedTemporaryFile("w", encoding="UTF-8", suffix=".bat", delete=False) as tf:
                # See https://stackoverflow.com/a/42622705
                tf.writelines(
                    [
                        "@echo off",
                        f"\nchdir {os.getcwd()}",
                        f"\n{sys.executable} -u {plugin_path.as_posix()}",
                    ],
                )

                tf.flush()

                plugin_path = Path(tf.name)
                atexit.register(os.remove, plugin_path)

        command = [
            sys.executable,
            "-m",
            "grpc.tools.protoc",
            f"--plugin=protoc-gen-custom={plugin_path.as_posix()}",
            "--experimental_allow_proto3_optional",
            "--custom_opt=pydantic_dataclasses",
            f"--proto_path={path.as_posix()}",
            f"--custom_out={output_dir.as_posix()}",
            *[p.as_posix() for p in path.glob("*.proto")],
        ]
    else:
        command = [
            sys.executable,
            "-m",
            "grpc.tools.protoc",
            f"--proto_path={path.as_posix()}",
            f"--{python_out_option}={output_dir.as_posix()}",
            *[p.as_posix() for p in path.glob("*.proto")],
        ]
    proc = await asyncio.create_subprocess_exec(
        *command,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE,
    )
    stdout, stderr = await proc.communicate()
    return stdout, stderr, proc.returncode
