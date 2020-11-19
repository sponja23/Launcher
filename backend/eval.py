from commands import command_table
from results import CommandResult, ObjectResult, SyntaxErrorResult, NoResult

current_environment = None

launcher_globals = {**command_table}


def eval_command(s: str) -> CommandResult:
    global launcher_globals

    statement = False
    try:
        code = compile(s, "<string>", "eval")
    except SyntaxError:
        try:
            code = compile(s, "<string>", "exec")
            statement = True
        except SyntaxError as err:
            return SyntaxErrorResult(err)

    if statement:
        exec(code, launcher_globals)
        return NoResult()
    else:
        result = eval(code, launcher_globals)
        if result is None:
            return NoResult()
        elif isinstance(result, CommandResult):
            return result
        else:
            return ObjectResult(result)


if __name__ == "__main__":
    while True:
        print(str(eval_command(input("> "))))
