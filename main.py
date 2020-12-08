from PyQt5.QtCore import Qt, pyqtSlot, Q_CLASSINFO
from PyQt5.QtWidgets import QApplication
from PyQt5.QtDBus import QDBusAbstractAdaptor, QDBusConnection
from UI import dbus_options
from UI.main_window import MainWindow
from UI.result_handlers import result_handlers, handle_default
from UI.history import History
from backend.eval import eval_command
from backend.launcher_globals import launcher_globals


hist = History()


def onReturnPressed(window: MainWindow, text: str) -> None:
    if text != "":
        hist.push(text)
    result = eval_command(text)
    result_handlers.get(type(result), handle_default)(window, result)


def onTextChanged(window: MainWindow, text: str) -> None:
    hist.reset_index()
    if(launcher_globals["debug"]):
        print(f"Text changed: {text}")


def onKeyPressed(window: MainWindow, key: Qt.Key, modifiers: Qt.KeyboardModifiers) -> bool:
    if key == Qt.Key_Tab:
        print("Pressed Tab")
    elif key == Qt.Key_Up and (modifiers & Qt.ControlModifier or True):  # Placeholder for window.currentResult != list
        window.input.setText(hist.get_prev())
    elif key == Qt.Key_Down and (modifiers & Qt.ControlModifier or True):
        window.input.setText(hist.get_next())
    elif key == Qt.Key_Q and modifiers & Qt.ControlModifier:
        exit()
    elif key == Qt.Key_A and modifiers & Qt.ControlModifier:
        window.input.selectAll()
    else:
        return False
    return True


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
