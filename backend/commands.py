from typing import Callable, Any, Dict, Union

Command = Callable[..., Any]


command_table: Dict[str, Command] = {}


def command(arg: Union[str, Command]) -> Union[Callable[[Command], Command], Command]:
    if type(arg) is str:
        name = arg

        def decorator(func: Command) -> Command:
            func.is_command = True
            command_table[name] = func
            return func

        return decorator
    else:
        arg.is_command = True
        command_table[arg.__name__] = arg
        return arg


@command
def test(x=5):
    return x + 1