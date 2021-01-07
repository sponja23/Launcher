import os
import subprocess
from ..base import command
from ..results import ListResult, TextResult
from .autocompletion import directory_autocomplete, file_autocomplete


# TODO: Error handling


def process_path(path: str) -> str:
    return os.path.expandvars(os.path.expanduser(path))


@command
def pwd() -> TextResult:
    return TextResult(os.getcwd())


@command(autocomplete=lambda i, s: directory_autocomplete(s))
def ls(path: str = '.') -> ListResult:
    path = process_path(path)
    return ListResult(os.listdir(path))


@command(autocomplete=lambda i, s: directory_autocomplete(s))
def cd(path: str) -> None:
    path = process_path(path)
    os.chdir(path)


@command(autocomplete=lambda i, s: file_autocomplete(s))
def op(path: str) -> None:
    path = process_path(path)
    subprocess.run(["xdg-open", os.path.expanduser(path)])
