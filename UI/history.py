from typing import List


class History:
    def __init__(self: "History") -> None:
        self.commands: List[str] = []
        self.current_index: int = 0

    def push(self: "History", cmd: str) -> None:
        if len(self.commands) == 0 or cmd != self.commands[-1]:
            self.commands.append(cmd)
        self.reset_index()

    def get_prev(self: "History") -> str:
        if self.current_index > 0:
            self.current_index -= 1
            return self.commands[self.current_index]
        else:
            return self.commands[0]

    def get_next(self: "History") -> str:
        if self.current_index < len(self.commands) - 1:
            self.current_index += 1
            return self.commands[self.current_index]
        else:
            self.current_index = len(self.commands)
            return ""

    def reset_index(self: "History") -> None:
        self.current_index = len(self.commands)
