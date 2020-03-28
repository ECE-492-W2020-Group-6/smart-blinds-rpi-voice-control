"""
Date: Mar 27, 2020
Author: Ishaat Chowdhury
Contents: Contains tests for position command
"""

import pytest
from rpi_voice_control.command.position import PositionCommand
from rpi_voice_control.constants import DEFAULT_RPI_SERVER_IP, DEFAULT_RPI_SERVER_PORT

""" Tests for invalid input
"""
@pytest.mark.parametrize("input_text", [
    (""),
    ("move blind -10.571%"),
    ("move blind 20m"),
    ("move blind -12.16% -13.13%"),
    ("move blind 20m 12h"),
    ("move blind 10.13% 20.17% 2m 13h"),
])
def test_position_command_builder_invalid_text(input_text):
    command = PositionCommand.build(input_text)
    assert command is None

""" Tests for valid input with default ip/port
"""
@pytest.mark.parametrize("input_text,expected", [
    ("move blind 12.197% 10m", PositionCommand(12.197, 10)),
])
def test_position_command_builder_defaults(input_text, expected):
    command = PositionCommand.build(input_text) 
    assert isinstance(command, PositionCommand)
    assert command == expected

""" Tests for valid input with specified ip/port
"""
@pytest.mark.parametrize("input_text,ip,port,expected", [
    ("move blind -91.129% 12h", "192.167.1.254", 9112, PositionCommand(-91.129, 12 * 60, ip="192.167.1.254", port=9112))
])
def test_position_command_builder(input_text, ip, port, expected):
    command = PositionCommand.build(input_text, ip=ip, port=port) 
    assert isinstance(command, PositionCommand)
    assert command == expected
