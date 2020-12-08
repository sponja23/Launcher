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


@command
def ls(path: str = '.') -> ListResult:
    path = process_path(path)
    return ListResult(os.listdir(path))


ls.autocomplete = lambda i, s: directory_autocomplete(s)


@command
def cd(path: str) -> None:
    path = process_path(path)
    os.chdir(path)


cd.autocomplete = lambda i, s: directory_autocomplete(s)


@command
def op(path: str) -> None:
    path = process_path(path)
    subprocess.run(["xdg-open", os.path.expanduser(path)])


op.autocomplete = lambda i, s: file_autocomplete(s)
