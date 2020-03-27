"""
Date: Mar 27, 2020
Author: Ishaat Chowdhury
Contents: Contains unit tests for voice parser
"""

import pytest
from rpi_voice_control.voice_parser import VoiceParser

@pytest.mark.parametrize("input_line,expected", [
    # Unchanged
    ("", ""),
    ("hello world", "hello world"),
    # Positive Integers
    ("move blinds to ten percent", "move blind 10 percent"),
    ("move blinds to ninety five percent", "move blind 95 percent"),
    ("move blinds to fourteen percent", "move blind 14 percent"),
    # Positive Decimals
    ("move blinds to five point three percent", "move blind 5.3 percent"),
    ("move blinds to eighty-seven point seventeen percent", "move blind 87.17 percent"),
    ("move blinds to seventy one point three five percent", "move blind 71.35 percent"),
    # Negative Integers
    ("move blinds to minus twelve percent", "move blind -12 percent"),
    ("move blinds to minus sixty three percent", "move blind -63 percent"),
    ("move blinds to minus fifteen percent", "move blind -15 percent"),
    ("move blinds to negative four percent", "move blind -4 percent"),
    ("move blinds to negative forty-nine percent", "move blind -49 percent"),
    ("move blinds to negative one hundred percent", "move blind -100 percent"),
    # Negative Decimals
    ("move blinds to minus eighteen point nineteen percent", "move blind -18.19 percent"),
    ("move blinds to minus twenty seven point one three six percent", "move blind -27.136 percent"),
    ("move blinds to minus seven point two percent", "move blind -7.2 percent"),
    ("move blinds to negative four point five eight percent", "move blind -4.58 percent"),
    ("move blinds to negative three three point seventy-seven percent", "move blind -33.77 percent"),
    ("move blinds to negative eleven point three five one percent", "move blind -11.351 percent"),
])
def test_parse_voice(input_line, expected):
    result = VoiceParser.parse(input_line)
    assert result == expected
