from rpi_voice_control.command.command import Command
import re

class PositionCommand(Command):
    PATTERN = re.compile(r"move blind (-?\d+(?:.\d+)?)% (\d+)(m|h)")

    def __init__(self, position, duration):
        self._mode = 4 # Manual
        self._position = position
        self._duration = duration

    def __eq__(self, other):
        if isinstance(other, PositionCommand):
            return self._mode == other._mode \
                and self._position == other._position \
                and self._duration == other._duration
        return False

    def __str__(self):
        return "PositionCommand(mode={}, position={}, duration={})".format(
            self._mode, self._duration, self._position)

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
