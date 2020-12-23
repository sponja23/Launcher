from typing import Any, Mapping
import os
import json
import atexit


FILE_DIRECTORY = os.path.dirname(os.path.abspath(__file__))
settings: Mapping[str, Any] = {}


def load_settings() -> None:
    global settings
    with open(os.path.join(FILE_DIRECTORY, "..", "user_data", "settings.json"), 'r') as settings_file:
        settings = json.load(settings_file)


@atexit.register
def save_settings() -> None:
    with open(os.path.join(FILE_DIRECTORY, "..", "user_data", "settings.json"), 'w') as settings_file:
        json.dump(settings, settings_file, indent=4)


load_settings()
