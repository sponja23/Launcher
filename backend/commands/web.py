import webbrowser
import requests
from ..base import Command, command
from ..results import NoResult
from ..launcher_globals import launcher_globals

Command.table["get_request"] = Command(requests.get, name="get_request")
Command.table["post_request"] = Command(requests.post, name="post_request")


@command
def open_page(url: str) -> None:
    webbrowser.get().open(url)
    launcher_globals["window"].setVisible(False)
