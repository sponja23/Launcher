from .launcher_globals import launcher_globals
from .results import CommandResult, ObjectResult, SyntaxErrorResult, NoResult
from .base import Command
from .commands import *

launcher_globals.update(Command.table)


def eval_directive(s: str) -> CommandResult:
    return NoResult()


def eval_statement(s: str) -> CommandResult:
    code = compile(s, "<string>", "exec")
    exec(code, launcher_globals)
    return NoResult()


def eval_expr(s: str) -> CommandResult:
    code = compile(s, "<string>", "eval")
    result = eval(code, launcher_globals)

    if type(result) is Command:
        result = result()

    if result is None:
        return NoResult()
    elif isinstance(result, CommandResult):
        return result
    else:
        return ObjectResult(result)


def eval_command(s: str) -> CommandResult:
    if s[0] == "#":
        return eval_directive(s[1:])
    try:
        return eval_expr(s)
    except SyntaxError:
        try:
            return eval_statement(s)
        except SyntaxError as err:
            return SyntaxErrorResult(err)
    print("error")
    return NoResult()


if __name__ == "__main__":
    while True:
        print(str(eval_command(input("> "))))
