from ..base import command
from ..results import NoResult
from ..launcher_globals import launcher_globals
from ..history import history
from pprint import pprint


@command
def print_vars() -> NoResult:
    pprint(launcher_globals)
    return NoResult()


@command
def print_history() -> NoResult:
    pprint(history.commands)
    print(f"Index: {history.current_index}")