from typing import List


class CommandTime:

    def __init__(self, formatted_time, raw_time) -> None:
        self.formatted_time = formatted_time
        self.raw_time = raw_time


class Command:

    def __init__(self, sender_name: str, sender_steamid: int, time: CommandTime, command: str, args: List[str]) -> None:
        self.sender_name = sender_name
        self.sender_steamid = sender_steamid
        self.time = time
        self.command = command
        self.args = args
