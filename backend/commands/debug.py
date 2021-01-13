from pprint import pprint
from ..base import command
from ..launcher_globals import launcher_globals
from ..history import history


@command
def print_vars() -> None:
    pprint(launcher_globals)


@command
def print_history() -> None:
    pprint(history.commands)
    print(f"Index: {history.current_index}")
