"""
Date: Mar 27, 2020
Author: Ishaat Chowdhury
Contents: Contains tests for CommandFactory
"""
import pytest
from rpi_voice_control.command.command_factory import CommandFactory
from rpi_voice_control.command.position import PositionCommand
from rpi_voice_control.constants import DEFAULT_RPI_SERVER_IP, DEFAULT_RPI_SERVER_PORT

""" Tests for invalid input
"""
@pytest.mark.parametrize("input_text", [
    (""),
    ("las;lkfjkdsajflkjsalkfjalfkjf"),
])
def test_command_factory_invalid_input(input_text):
    command = CommandFactory.build(input_text)
    assert command is None

""" Tests for valid input with default ip/port
"""
@pytest.mark.parametrize("input_text,expected", [
    ("move blind 15.15% 90m", PositionCommand(15.15, 90)),
])
def test_command_factory_default(input_text, expected):
    command = CommandFactory.build(input_text)
    assert isinstance(command, expected.__class__)
    assert command == expected

""" Tests for valid input with specified ip/port
"""
@pytest.mark.parametrize("input_text,ip,port,expected", [
    ("move blind -18.4531% 16h", "192.167.1.254", 9112, PositionCommand(-18.4531, 16 * 60, ip="192.167.1.254", port=9112)),
])
def test_command_factory(input_text, ip, port, expected):
    command = CommandFactory.build(input_text, ip=ip, port=port)
    assert isinstance(command, expected.__class__)
    assert command == expected
