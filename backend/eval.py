from .launcher_globals import launcher_globals
from .results import CommandResult, ObjectResult, ErrorResult, NoResult, BashResult
from .base import Command
from .bash import run_bash


def eval_directive(s: str) -> CommandResult:
    return NoResult()


def eval_bash(s: str) -> CommandResult:
    return BashResult(run_bash(s))


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
    else:
        launcher_globals["last"] = result
        if isinstance(result, CommandResult):
            return result
        else:
            return ObjectResult(result)


def eval_command(s: str) -> CommandResult:
    if s == "":
        return NoResult()
    elif s[0] == "#":
        return eval_directive(s[1:])
    elif s[0] == ">":
        return eval_bash(s[1:].strip())
    try:
        return eval_expr(s)
    except SyntaxError:
        try:
            return eval_statement(s)
        except (NameError, SyntaxError) as err:
            return ErrorResult(err)
    except NameError as err:
        return ErrorResult(err)
    return NoResult()


if __name__ == "__main__":
    while True:
        print(str(eval_command(input("> "))))
