from code import InteractiveConsole
from ..base import command
from ..launcher_globals import launcher_globals


def custom_exit_function():
    raise SystemExit


@command
def terminal() -> None:
    launcher_globals["exit"] = custom_exit_function
    console = InteractiveConsole(locals=launcher_globals)

    try:
        console.interact(banner="Use exit() to return to launcher")
    except SystemExit:
        pass

    del launcher_globals["exit"]
