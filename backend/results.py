from abc import ABC
from typing import Any, Dict, List, Callable, Optional


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


class ErrorResult(CommandResult):
    def __init__(self: "ErrorResult", err: BaseException) -> None:
        self.err = err

    def __str__(self: "ErrorResult") -> str:
        return f"ErrorResult({str(self.err)})"


class TextResult(CommandResult):
    def __init__(self: "TextResult", text: str, *,
                 options: Dict[str, Any] = {}) -> None:
        self.text = text
        self.options = options

    def __str__(self: "TextResult") -> str:
        return f"TextResult(\"{self.text}\")"


class ListResult(CommandResult):
    def __init__(self: "ListResult", lst: List[Any], *,
                 options: Dict[str, Any] = {},
                 item_function: Optional[Callable[[int, str], None]] = None) -> None:
        self.lst = lst
        self.options = options
        self.item_function = item_function

    def __str__(self: "ListResult") -> str:
        return f"ListResult(\"{str(self.lst)}\")"


class LatexResult(CommandResult):
    def __init__(self: "LatexResult", expr: str) -> None:
        self.expr = expr

    def __str__(self: "LatexResult") -> str:
        return f"LatexResult(\"{self.expr}\")"


class BashResult(CommandResult):
    def __init__(self: "BashResult", text: str) -> None:
        self.text = text

    def __str__(self: "BashResult") -> str:
        return f"BashResult(\"{self.text}\")"
