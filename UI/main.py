from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QWidget, QGraphicsDropShadowEffect,
                             QFrame, QVBoxLayout, QLayout, QLineEdit, QLabel)
from PyQt5.Qt import QColor
from typing import Iterable, Mapping, Any
import os


FILE_DIRECTORY = os.path.dirname(os.path.abspath(__file__))


app = QApplication([])


class MainWindow(QWidget):
    def __init__(self: "MainWindow", *args: Iterable[Any], **kwargs: Mapping[str, Any]) -> None:
        super().__init__(*args, **kwargs)

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
        self.createResultLabel()

        self.currentResult = None

        with open(os.path.join(FILE_DIRECTORY, "style.qss"), 'r') as style_file:
            self.setStyleSheet(style_file.read())

    def createFrame(self: "MainWindow") -> None:
        self.frame = QFrame(self)
        self.frame.setObjectName("frame")
        self.frameLayout = QVBoxLayout(self.frame)
        self.frameLayout.setContentsMargins(0, 0, 0, 0)
        self.frame.setLayout(self.frameLayout)
        self.windowLayout.addWidget(self.frame)

    def createInput(self: "MainWindow") -> None:
        self.input = QLineEdit(self)
        self.input.setObjectName("input")
        self.input.returnPressed.connect(self.toggleResultLabel)
        self.frameLayout.addWidget(self.input)

    def createResultLabel(self: "MainWindow") -> None:
        self.resultLabel = QLabel("[1, 4, 9, 16]")
        self.resultLabel.setObjectName("resultLabel")
        self.frameLayout.addWidget(self.resultLabel)


window = MainWindow()
window.show()

app.exec_()
