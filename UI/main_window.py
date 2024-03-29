from PyQt5.QtCore import Qt, QPoint
from PyQt5.QtWidgets import (QWidget, QGraphicsDropShadowEffect, QFrame,
                             QVBoxLayout, QLayout, QLineEdit, QLabel, QApplication)
from PyQt5.Qt import QColor
from PyQt5.QtGui import QKeyEvent, QCursor
from typing import Iterable, Mapping, Any, Callable, Optional
from .results_list import ResultsList
import os


FILE_DIRECTORY = os.path.dirname(os.path.abspath(__file__))
with open(os.path.join(FILE_DIRECTORY, "style.qss"), 'r') as style_file:
    style_sheet = style_file.read()


class LineInput(QLineEdit):
    def __init__(self: "LineInput", *args: Iterable[Any],
                 window: "MainWindow",
                 keyPressedHandler: Callable[["MainWindow", Qt.Key], bool],
                 **kwargs: Mapping[str, Any]) -> None:
        super().__init__(*args, **kwargs)
        self.window = window
        self.keyPressedHandler = keyPressedHandler

    def keyPressEvent(self: "LineInput", event: QKeyEvent) -> None:
        if not self.keyPressedHandler(self.window, event.key(), event.modifiers()):
            super().keyPressEvent(event)


class MainWindow(QWidget):
    def __init__(self: "MainWindow", *args: Iterable[Any],
                 returnPressedHandler: Callable[["MainWindow", str], None],
                 textChangedHandler: Callable[["MainWindow", str], None],
                 keyPressedHandler: Callable[["MainWindow", Qt.Key], bool],
                 **kwargs: Mapping[str, Any]) -> None:
        super().__init__(*args, **kwargs)
        self.setWindowTitle("Launcher")

        self.returnPressedHandler = returnPressedHandler
        self.textChangedHandler = textChangedHandler
        self.keyPressedHandler = keyPressedHandler

        self.setObjectName("window")
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.moveToCenter()

        effect = QGraphicsDropShadowEffect()
        effect.setBlurRadius(20)
        effect.setColor(QColor(0, 0, 0, 192))
        effect.setXOffset(0)
        effect.setYOffset(3)
        self.setGraphicsEffect(effect)

        self.windowLayout = QVBoxLayout(self)
        self.windowLayout.setSizeConstraint(QLayout.SetFixedSize)
        self.windowLayout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(self.windowLayout)

        self.createFrame()
        self.createInput()
        self.createTextResult()
        self.createImageResult()
        self.createErrorResult()
        self.createBashResult()
        self.createListResult()

        self.currentResult: Optional[QWidget] = None

        self.input.textChanged.connect(self.onTextChange)
        self.input.returnPressed.connect(self.onReturnPressed)

        self.setStyleSheet(style_sheet)

    def moveToCenter(self: "MainWindow") -> None:
        dw = QApplication.desktop()
        self.move(dw.screenGeometry(dw.screenNumber(QCursor.pos())).center()
                  - QPoint(self.rect().right() / 2, 256))

    def createFrame(self: "MainWindow") -> None:
        self.frame = QFrame(self)
        self.frame.setObjectName("frame")
        self.frameLayout = QVBoxLayout(self.frame)
        self.frameLayout.setContentsMargins(0, 0, 0, 0)
        self.frame.setLayout(self.frameLayout)
        self.windowLayout.addWidget(self.frame)

    def createInput(self: "MainWindow") -> None:
        self.input = LineInput(self, window=self, keyPressedHandler=self.keyPressedHandler)
        self.input.setObjectName("input")
        self.frameLayout.addWidget(self.input)

    def createTextResult(self: "MainWindow") -> None:
        self.textResult = QLabel(self)
        self.textResult.setObjectName("textResult")
        self.textResult.setVisible(False)
        self.frameLayout.addWidget(self.textResult)

    def createImageResult(self: "MainWindow") -> None:
        self.imageResult = QLabel(self)
        self.imageResult.setObjectName("imageResult")
        self.imageResult.setAlignment(Qt.AlignHCenter)
        self.imageResult.setVisible(False)
        self.frameLayout.addWidget(self.imageResult)

    def createErrorResult(self: "MainWindow") -> None:
        self.errorResult = QLabel(self)
        self.errorResult.setObjectName("errorResult")
        self.errorResult.setVisible(False)
        self.frameLayout.addWidget(self.errorResult)

    def createBashResult(self: "MainWindow") -> None:
        self.bashResult = QLabel(self)
        self.bashResult.setObjectName("bashResult")
        self.bashResult.setWordWrap(True)
        self.bashResult.setVisible(False)
        self.frameLayout.addWidget(self.bashResult)

    def createListResult(self: "MainWindow") -> None:
        self.listResult = ResultsList(self)
        self.listResult.setObjectName("listResult")
        self.listResult.setVisible(False)
        self.frameLayout.addWidget(self.listResult)

    def onReturnPressed(self: "MainWindow") -> None:
        text = self.input.text()
        self.input.setText("")
        self.returnPressedHandler(self, text)

    def onTextChange(self: "MainWindow", text: str) -> None:
        self.textChangedHandler(self, text)

    def setResultWidget(self: "MainWindow", resultWidget: Optional[QWidget]) -> None:
        if self.currentResult is not None:
            self.currentResult.setVisible(False)
        self.currentResult = resultWidget
        if self.currentResult is not None:
            self.currentResult.setVisible(True)

    def keyPressEvent(self: "ResultsList", event: QKeyEvent) -> None:
        if event.key() == Qt.Key_E and event.modifiers() & Qt.ControlModifier:
            self.input.setFocus()
