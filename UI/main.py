from main_window import MainWindow
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication


def onReturnPressed(window: MainWindow, text: str) -> None:
    window.textResult.setText(text)


def onTextChanged(window: MainWindow, text: str) -> None:
    print(f"Text changed: {text}")


def onKeyPressed(window: MainWindow, key: Qt.Key) -> bool:
    if key == Qt.Key_Tab:
        print("Pressed Tab")
        print(type(window))
        return True
    return False


app = QApplication([])

window = MainWindow(
            returnPressedHandler=onReturnPressed,
            textChangedHandler=onTextChanged,
            keyPressedHandler=onKeyPressed
         )
window.show()

app.exec_()
