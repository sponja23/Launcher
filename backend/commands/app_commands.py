from typing import Iterable, Mapping, Any
from functools import partial
from os import path
import json
import re
import subprocess
from ..base import Command, USER_DATA_DIR
from ..results import NoResult
from ..launcher_globals import launcher_globals


APPS_PATH = path.join(USER_DATA_DIR, "apps.json")
apps = []


path_var_regex = re.compile(r"\$(\w+)")


def save_apps() -> None:
    global apps
    with open(APPS_PATH, 'w') as apps_file:
        json.dump(apps, apps_file, indent=4)


def substitute_var(m: re.Match, *, __positional_args: Iterable[Any],
                   **kwargs: Mapping[str, Any]) -> str:
    identifier = m.group(1)
    if identifier.isnumeric():
        index = int(identifier)
        if index < len(__positional_args):
            return str(__positional_args[index])
        else:
            return ""
    else:
        return str(kwargs.get(identifier, ""))


def exec_app(path: str, *args: Iterable[Any], **kwargs: Mapping[str, Any]) -> None:
    path = re.sub(path_var_regex, partial(substitute_var, __positional_args=args, **kwargs), path)
    subprocess.run(path, shell=True)
    launcher_globals["window"].setVisible(False)


if path.exists(APPS_PATH):
    with open(APPS_PATH, 'r') as apps_file:
        apps = json.load(apps_file)
else:
    save_apps()


for app in apps:
    func = partial(exec_app, app["exec"])
    cmd = Command(func, name=app["name"])
    Command.table[cmd.name] = cmd
    for alias in app.get("aliases", []):
        Command.table[alias] = cmd
