from dataclasses import dataclass

from .plugin.typing_compiler import TypingCompiler


@dataclass
class Settings:
    pydantic_dataclasses: bool
    typing_compiler: TypingCompiler
