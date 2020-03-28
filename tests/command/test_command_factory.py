import pytest
from rpi_voice_control.command.command_factory import CommandFactory
from rpi_voice_control.command.position import PositionCommand

@pytest.mark.parametrize("input_text", [
    (""),
    ("las;lkfjkdsajflkjsalkfjalfkjf"),
])
def test_command_factory_invalid_input(input_text):
    command = CommandFactory.build(input_text)
    assert command is None

@pytest.mark.parametrize("input_text,expected", [
    ("move blind 15.15% 90m", PositionCommand(15.15, 90)),
    ("move blind -18.4531% 16h", PositionCommand(-18.4531, 16 * 60)),
])
def test_command_factory(input_text, expected):
    command = CommandFactory.build(input_text)
    assert isinstance(command, expected.__class__)
    assert command == expected
