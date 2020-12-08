from typing import Any, Dict, Callable
from .main_window import MainWindow
from backend.results import (CommandResult, NoResult, TextResult, ListResult,
                             ErrorResult, ObjectResult, LatexResult)


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


def handle_default(window: MainWindow, result: CommandResult) -> None:
    window.setResultWidget(window.textResult)
    window.textResult.setText(str(result))


result_handlers: Dict[type, Callable[[MainWindow, CommandResult], None]] = {
    TextResult: handle_text,
    ObjectResult: handle_object,
    ErrorResult: handle_error,
    NoResult: handle_none,
    CommandResult: handle_default
}
