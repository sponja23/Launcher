from PyQt5.QtCore import Qt, pyqtSlot, Q_CLASSINFO, QPoint
from PyQt5.QtWidgets import QApplication
from PyQt5.QtDBus import QDBusAbstractAdaptor, QDBusConnection
from PyQt5.QtGui import QCursor
from .main_window import MainWindow
from backend.eval import eval_command
from . import dbus_options


def onReturnPressed(window: MainWindow, text: str) -> None:
    window.textResult.setText(str(eval_command(text)))


def onTextChanged(window: MainWindow, text: str) -> None:
    print(f"Text changed: {text}")


def onKeyPressed(window: MainWindow, key: Qt.Key) -> bool:
    if key == Qt.Key_Tab:
        print("Pressed Tab")
        window.setVisible(False)
        return True
    return False


app = QApplication([])
app.setApplicationName("launcher")
app.setApplicationDisplayName("Launcher")
app.setQuitOnLastWindowClosed(False)

window = MainWindow(
            returnPressedHandler=onReturnPressed,
            textChangedHandler=onTextChanged,
            keyPressedHandler=onKeyPressed
         )


class ServerAdaptor(QDBusAbstractAdaptor):
    Q_CLASSINFO("D-Bus Interface", "org.sponja.launcher.server")

    @pyqtSlot(int)
    def setVisible(self: "ServerAdaptor", option: int) -> None:
        if option == dbus_options.HIDE:
            window.setVisible(False)
        elif option == dbus_options.SHOW:
            window.setVisible(True)
        elif option == dbus_options.TOGGLE:
            window.setVisible(not window.isVisible())
        else:
            raise NotImplementedError

        if window.isVisible():
            window.moveToCenter()
            window.activateWindow()


adaptor = ServerAdaptor(window)
QDBusConnection.sessionBus().registerObject("/", window)

if not QDBusConnection.sessionBus().registerService("org.sponja.launcher"):
    print(f"DBus error: {QDBusConnection.sessionBus().lastError().type()}")
