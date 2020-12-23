from typing import Any, Dict, Callable
from .main_window import MainWindow
from backend.results import (CommandResult, NoResult, TextResult, ListResult,
                             ErrorResult, ObjectResult, LatexResult, BashResult)


def handle_text(window: MainWindow, result: TextResult) -> None:
    window.setResultWidget(window.textResult)
    window.textResult.setText(result.text)


def handle_object(window: MainWindow, result: ObjectResult) -> None:
    window.setResultWidget(window.textResult)
    window.textResult.setText(str(result.obj))


def handle_error(window: MainWindow, result: ErrorResult) -> None:
    window.setResultWidget(window.errorResult)
    window.errorResult.setText(f"Error: {str(result.err)}")


def handle_none(window: MainWindow, result: NoResult) -> None:
    window.setResultWidget(None)


def handle_bash(window: MainWindow, result: BashResult) -> None:
    window.setResultWidget(window.bashResult)
    window.bashResult.setText(result.text)


def handle_default(window: MainWindow, result: CommandResult) -> None:
    window.setResultWidget(window.textResult)
    window.textResult.setText(str(result))


def handle_list(window: MainWindow, result: ListResult) -> None:
    window.setResultWidget(window.listResult)
    window.listResult.setList([str(elem) for elem in result.lst])
    window.listResult.setCurrentIndex(window.listResult.model().index(0, 0))
    window.listResult.setFocus()


result_handlers: Dict[type, Callable[[MainWindow, CommandResult], None]] = {
    TextResult: handle_text,
    ObjectResult: handle_object,
    ErrorResult: handle_error,
    BashResult: handle_bash,
    NoResult: handle_none,
    CommandResult: handle_default,
    ListResult: handle_list
}
