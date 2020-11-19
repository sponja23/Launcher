from abc import ABC
from typing import Any


class CommandResult(ABC):
    pass


class NoResult(CommandResult):
    def __str__(self: "NoResult") -> str:
        return "NoResult()"


class ObjectResult(CommandResult):
    def __init__(self: "ObjectResult", obj: Any) -> None:
        self.obj = obj

    def __str__(self: "ObjectResult") -> str:
        return f"ObjectResult({str(self.obj)})"


class SyntaxErrorResult(CommandResult):
    def __init__(self: "SyntaxErrorResult", err: SyntaxError) -> None:
        self.err = err

    def __str__(self: "SyntaxErrorResult") -> str:
        return f"SyntaxErrorResult({str(self.err)})"
