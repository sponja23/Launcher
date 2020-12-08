from PyQt5.QtDBus import QDBusConnection, QDBusInterface, QDBus
from argparse import ArgumentParser
import dbus_options

parser = ArgumentParser(description="Launcher controller")
parser.add_argument("--show", dest="option", action="store_const", const=dbus_options.SHOW)
parser.add_argument("--hide", dest="option", action="store_const", const=dbus_options.HIDE)
parser.add_argument("--toggle", dest="option", action="store_const", const=dbus_options.TOGGLE)

args = parser.parse_args()

interface = QDBusInterface("org.sponja.launcher", "/", "org.sponja.launcher.server", QDBusConnection.sessionBus())


if not interface.isValid():
    print(f"DBus error: {QDBusConnection.sessionBus().lastError().message()}")
else:
    interface.call(QDBus.NoBlock, "setVisible", 2)
