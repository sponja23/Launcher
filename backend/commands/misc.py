from ..base import command
from ..results import NoResult
from ..launcher_globals import launcher_globals
from pprint import pprint


@command
def print_vars() -> NoResult:
    pprint(launcher_globals)
    return NoResult()
