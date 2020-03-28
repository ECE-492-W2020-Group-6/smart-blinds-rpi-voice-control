from rpi_voice_control.command.command import Command
import re

class PositionCommand(Command):
    PATTERN = re.compile(r"move blind (-?\d+(?:.\d+)?)% (\d+)(m|h)")

    def __init__(self, position, duration):
        self._payload = {
            "mode": 4, # Manual
            "position": position,
            "duration": duration,
        }

    @property
    def payload(self):
        return self._payload

    def __eq__(self, other):
        if isinstance(other, PositionCommand):
            return self.payload == other.payload
        return False

    def run(self):
        pass

    @classmethod
    def build(cls, text):
        match = cls.PATTERN.fullmatch(text)
        if match:
            position = float(match.group(1))
            duration = int(match.group(2)) * 60 \
                if match.group(3) == "h" else int(match.group(2))
            return PositionCommand(position, duration)
        return None
