from typing import Callable, Any, Dict, Optional, Union, Iterable, Mapping
from os import path
from .settings import settings
from .results import CommandResult


CommandFunction = Callable[..., CommandResult]
AutocompleteFunction = Callable[[int, str], Iterable[str]]


class Command:
    table: Dict[str, "Command"] = {}

    def __init__(self: "Command",
                 function: CommandFunction,
                 **kwargs: Mapping[str, Any]) -> None:
        self.function = function
        if hasattr(function, "__name__"):
            self.name = kwargs.get("name", function.__name__)
        else:
            self.name = kwargs["name"]
        self.autocomplete: AutocompleteFunction = kwargs.get("autocomplete", None)

    def __call__(self: "Command",
                 *args: Iterable[Any],
                 **kwargs: Mapping[str, Any]) -> Any:
        return self.function(*args, **kwargs)


def command(func: Optional[CommandFunction] = None,
            **kwargs: Mapping[str, Any]) -> Union[Callable[[CommandFunction], Command], Command]:
    if kwargs:
        assert(func is None)

        def decorator(func: CommandFunction) -> Command:
            cmd = Command(func, **kwargs)
            Command.table[cmd.name] = cmd
            return cmd

        return decorator
    else:
        cmd = Command(func)
        Command.table[cmd.name] = cmd
        return cmd


# VARS
variables: Dict[str, Any] = {}


def add_variable(name: str, obj: Any) -> None:
    variables[name] = obj


add_variable("settings", settings)


# ALIASES
aliases: Dict[str, str] = {}


def add_alias(name: str, expansion: str) -> None:
    raise NotImplementedError


_FILE_DIRECTORY = path.dirname(path.abspath(__file__))
USER_DATA_DIR = path.abspath(path.join(_FILE_DIRECTORY, "..", "user_data"))
