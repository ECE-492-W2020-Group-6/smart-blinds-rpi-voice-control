import pytest
from rpi_voice_control.voice_parser import VoiceParser

@pytest.mark.parametrize("input_line,expected", [
    # Unchanged
    ("", ""),
    ("hello world", "hello world"),
    # Positive Integers
    ("move blinds to ten percent", "move blind to 10 percent"),
    ("move blinds to ninety five percent", "move blind to 95 percent"),
    ("move blinds to fourteen percent", "move blind to 14 percent"),
    # Positive Decimals
    ("move blinds to five point three percent", "move blind to 5.3 percent"),
    ("move blinds to eighty-seven point seventeen percent", "move blind to 87.17 percent"),
    ("move blinds to seventy one point three five percent", "move blind to 71.35 percent"),
    # Negative Integers
    ("move blinds to minus twelve percent", "move blind to -12 percent"),
    ("move blinds to minus sixty three percent", "move blind to -63 percent"),
    ("move blinds to minus fifteen percent", "move blind to -15 percent"),
    ("move blinds to negative four percent", "move blind to -4 percent"),
    ("move blinds to negative forty-nine percent", "move blind to -49 percent"),
    ("move blinds to negative one hundred percent", "move blind to -100 percent"),
    # Negative Decimals
    ("move blinds to minus eighteen point nineteen percent", "move blind to -18.19 percent"),
    ("move blinds to minus twenty seven point one three six percent", "move blind to -27.136 percent"),
    ("move blinds to minus seven point two percent", "move blind to -7.2 percent"),
    ("move blinds to negative four point five eight percent", "move blind to -4.58 percent"),
    ("move blinds to negative three three point seventy-seven percent", "move blind to -33.77 percent"),
    ("move blinds to negative eleven point three five one percent", "move blind to -11.351 percent"),
])
def test_parse_voice(input_line, expected):
    result = VoiceParser.parse(input_line)
    assert result == expected
