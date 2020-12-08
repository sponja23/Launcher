from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QWidget, QGraphicsDropShadowEffect, QFrame,
                             QVBoxLayout, QLayout, QLineEdit, QLabel)
from PyQt5.Qt import QColor
from PyQt5.QtGui import QKeyEvent
from typing import Iterable, Mapping, Any, Callable
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
        if not self.keyPressedHandler(self.window, event.key()):
            super().keyPressEvent(event)


class MainWindow(QWidget):
    def __init__(self: "MainWindow", *args: Iterable[Any],
                 returnPressedHandler: Callable[["MainWindow", str], None],
                 textChangedHandler: Callable[["MainWindow", str], None],
                 keyPressedHandler: Callable[["MainWindow", Qt.Key], bool],
                 **kwargs: Mapping[str, Any]) -> None:
        super().__init__(*args, **kwargs)

        self.returnPressedHandler = returnPressedHandler
        self.textChangedHandler = textChangedHandler
        self.keyPressedHandler = keyPressedHandler

        self.setObjectName("window")
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

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

        self.currentResult = None

        self.input.textChanged.connect(self.onTextChange)
        self.input.returnPressed.connect(self.onReturnPressed)

        self.setStyleSheet(style_sheet)

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
        self.textResult = QLabel()
        self.textResult.setObjectName("textResult")
        self.frameLayout.addWidget(self.textResult)

    def createImageResult(self: "MainWindow") -> None:
        self.imageResult = QLabel()
        self.imageResult.setAlignment(Qt.AlignHCenter)
        self.imageResult.setVisible(False)
        self.frameLayout.addWidget(self.imageResult)

    def onReturnPressed(self: "MainWindow") -> None:
        text = self.input.text()
        self.input.setText("")
        self.returnPressedHandler(self, text)

    def onTextChange(self: "MainWindow", text: str) -> None:
        self.textChangedHandler(self, text)
