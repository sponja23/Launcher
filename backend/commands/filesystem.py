import os
import subprocess
from ..base import command
from ..results import ListResult, TextResult
from .autocompletion import directory_autocomplete, file_autocomplete


# TODO: Error handling


@command
def pwd() -> TextResult:
    return TextResult(os.getcwd())


@command
def ls(path: str = '.') -> ListResult:
    return ListResult(os.listdir(path))


ls.autocomplete = lambda i, s: directory_autocomplete(s)


@command
def cd(path: str) -> None:
    os.chdir(path)


cd.autocomplete = lambda i, s: directory_autocomplete(s)


@command
def op(path: str) -> None:
    subprocess.run(["xdg-open", path])


op.autocomplete = lambda i, s: file_autocomplete(s)
