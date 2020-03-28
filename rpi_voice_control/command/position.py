"""
Date: Mar 27, 2020
Author: Ishaat Chowdhury
Contents: Specific command to move to position manually
"""
from rpi_voice_control.command.command import Command
import re
import requests
import logging

""" Class that encapsulates data and behaviour necessary to move
    blinds to specific position
"""
class PositionCommand(Command):
    PATTERN = re.compile(r"move blind (-?\d+(?:.\d+)?)% (\d+)(m|h)")

    """ Construtor

    Arguments:
        position {float} - position to set blinds to
        duration {duration} - how long to set blinds to position for in minutes
        port {int} - port of Smartblinds RPI server
        kwargs {dict} - other optional parameters to pass to superclass
    """
    def __init__(self, position, duration, **kwargs):
        super().__init__(**kwargs)
        self._mode = 4 # Manual
        self._position = position
        self._duration = duration

    """ Check if two PositionCommand objects are equal

    Arguments:
        other {PositionCommand} - instance of other object

    """
    def __eq__(self, other):
        if isinstance(other, PositionCommand):
            return super().__eq__(other) \
                and self._mode == other._mode \
                and self._position == other._position \
                and self._duration == other._duration
        return False

    """ Return string representation of object

    Returns:
        str - str serialization of ojbect
    """
    def __str__(self):
        return "PositionCommand(mode={}, position={}, duration={}, ip={}, port={})".format(
            self._mode, self._position, self._duration, self._ip, self._port)

    """ Run command encoded in this object
    """
    def run(self):
        try:
            requests.post(f"http://localhost:{self._port}/api/v1/command", data={
                "mode": self._mode,
                "position": self._position,
                "duration": self._duration,
            })
        except Exception as e:
            logging.exception("Unable to send position command to server")

    """ Builder method to build instance of class from parsed voice command (as text)

    Arguments:
        cls {PositionCommand} - class object
        text {str} - text representing voice command
        kwargs {dict} - other optional parameters to pass to superclass

    Returns:
        an instance of PositionCommand or None
    """
    @classmethod
    def build(cls, text, **kwargs):
        match = cls.PATTERN.fullmatch(text)
        if match:
            position = float(match.group(1))
            duration = int(match.group(2)) * 60 \
                if match.group(3) == "h" else int(match.group(2))
            return PositionCommand(position, duration, **kwargs)
        return None
