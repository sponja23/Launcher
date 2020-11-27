from typing import Callable, Any, Dict, Union, Iterable, Mapping

CommandFunction = Callable[..., Any]
AutocompleteFunction = Callable[[int, str], Iterable[str]]


class Command:
    table: Dict[str, "Command"] = {}

    def __init__(self: "Command",
                 name: str,
                 function: CommandFunction,
                 **kwargs: Mapping[str, Any]) -> None:
        Command.table[name] = self
        self.name = name
        self.function = function
        self.autocomplete: AutocompleteFunction = kwargs.get("autocomplete", None)

    def __call__(self: "Command",
                 *args: Iterable[Any],
                 **kwargs: Mapping[str, Any]) -> Any:
        return self.function(*args, **kwargs)


def command(arg: Union[str, CommandFunction]) -> Union[Callable[[CommandFunction], Command], Command]:
    if type(arg) is str:

        def decorator(func: Command) -> Command:
            return Command(arg, func)

        return decorator
    else:
        return Command(arg.__name__, arg)


# VARS
variables: Dict[str, Any] = {}


def add_variable(name: str, obj: Any) -> None:
    variables[name] = obj


# ALIASES
aliases: Dict[str, str] = {}


def add_alias(name: str, expansion: str) -> None:
    raise NotImplementedError
