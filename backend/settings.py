from typing import Any, Mapping
from os import path
import json
import atexit


_FILE_DIRECTORY = path.dirname(path.abspath(__file__))
SETTINGS_PATH = path.join(_FILE_DIRECTORY, "..", "user_data", "settings.json")

DEFAULT_SETTINGS = {
    "debug": False,
    "max_list_items": 5
}

settings: Mapping[str, Any] = {}


def load_settings() -> None:
    global settings
    if path.exists(SETTINGS_PATH):
        with open(SETTINGS_PATH, 'r') as settings_file:
            settings = json.load(settings_file)
    else:
        settings = DEFAULT_SETTINGS.copy()
        save_settings()


@atexit.register
def save_settings() -> None:
    with open(SETTINGS_PATH, 'w') as settings_file:
        json.dump(settings, settings_file, indent=4)


load_settings()
