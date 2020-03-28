import pytest
from rpi_voice_control.command.position import PositionCommand

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

@pytest.mark.parametrize("input_text,expected", [
    ("move blind 12.197% 10m", PositionCommand(12.197, 10)),
    ("move blind -91.129% 12h", PositionCommand(-91.129, 12 * 60))
])
def test_position_command_builder_invalid_text(input_text, expected):
    command = PositionCommand.build(input_text) 
    assert isinstance(command, PositionCommand)
    assert command == expected
