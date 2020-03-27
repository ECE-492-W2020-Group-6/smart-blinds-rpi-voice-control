import pytest
from rpi_voice_control.voice_parser import VoiceParser

@pytest.mark.parametrize("input_line,expected", [
    # Unchanged
    ("", ""),
    ("hello world", "hello world"),
    ("I'm 12 years old!", "I'm 12 years old!"),
    # Positive Integers
    ("move blinds to ten percent", "move blinds to 10 percent"),
    ("move blinds to ninety five percent", "move blinds to 95 percent"),
    ("move blinds to fourteen percent", "move blinds to 14 percent"),
    # Positive Decimals
    ("move blinds to five point three percent", "move blinds to 5.3 percent"),
    ("move blinds to eighty-seven point seventeen percent", "move blinds to 87.17 percent"),
    ("move blinds to seventy one point three five percent", "move blinds to 71.35 percent"),
    # Negative Integers
    ("move blinds to minus twelve percent", "move blinds to -12 percent"),
    ("move blinds to minus sixty three percent", "move blinds to -63 percent"),
    ("move blinds to minus fifteen percent", "move blinds to -15 percent"),
    ("move blinds to negative four percent", "move blinds to -4 percent"),
    ("move blinds to negative forty-nine percent", "move blinds to -49 percent"),
    ("move blinds to negative one hundred percent", "move blinds to -100 percent"),
    # Negative Decimals
    ("move blinds to minus eighteen point nineteen percent", "move blinds to -18.19 percent"),
    ("move blinds to minus twenty seven point one three six percent", "move blinds to -27.136 percent"),
    ("move blinds to minus seven point two percent", "move blinds to -7.2 percent"),
    ("move blinds to negative four point five eight percent", "move blinds to -4.58 percent"),
    ("move blinds to negative three three point seventy-seven percent", "move blinds to -33.77 percent"),
    ("move blinds to negative eleven point three five one percent", "move blinds to -11.351 percent"),
])
def test_parse_voice(input_line, expected):
    result = VoiceParser.parse(input_line)
    assert result == expected
