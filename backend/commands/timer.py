from notifypy import Notify
from threading import Timer
from typing import Union
import re
from ..base import command


pattern = re.compile(r"^(\d*\.\d+|\d+)([dhms])?$")
units = {
    "s": 1,
    "m": 60,
    "h": 3600,
    "d": 86400
}


@command
def set_timer(time: Union[str, int, float], message: str = "Timer finished") -> None:
    if type(time) is str:
        match = pattern.match(time)

        if match is None:
            raise SyntaxError(f"Incorrect time format: {time}")

        amount = float(match.group(1))
        unit = match.group(2) or "s"
    elif type(time) in (int, float):
        amount = time
        unit = "s"

    notification = Notify()
    notification.title = "Timer"
    notification.message = message

    Timer(amount * units[unit], notification.send).start()
