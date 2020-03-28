"""
Date: Mar 27, 2020
Author: Ishaat Chowdhury
Contents: Contains unit tests for voice parser
"""

import pytest
from rpi_voice_control.voice_parser import VoiceParser

""" Runs tests for voice parser
"""
@pytest.mark.parametrize("input_line,expected", [
    # Unchanged
    ("", ""),
    ("hello world", "hello world"),
    # Positive Integers
    ("move blinds to ten percent", "move blind 10%"),
    ("move blinds to ninety five per cent", "move blind 95%"),
    ("move blinds to fourteen percent", "move blind 14%"),
    # Positive Decimals
    ("move blinds to five point three per cent", "move blind 5.3%"),
    ("move blinds to eighty-seven point seventeen percent", "move blind 87.17%"),
    ("move blinds to seventy one point three five per cent", "move blind 71.35%"),
    # Negative Integers
    ("move blinds to minus twelve percent", "move blind -12%"),
    ("move blinds to minus sixty three per cent", "move blind -63%"),
    ("move blinds to minus fifteen percent", "move blind -15%"),
    ("move blinds to negative four per cent", "move blind -4%"),
    ("move blinds to negative forty-nine percent", "move blind -49%"),
    ("move blinds to negative one hundred per cent", "move blind -100%"),
    # Negative Decimals
    ("move blinds to minus eighteen point nineteen percent", "move blind -18.19%"),
    ("move blinds to minus twenty seven point one three six per cent", "move blind -27.136%"),
    ("move blinds to minus seven point two percent", "move blind -7.2%"),
    ("move blinds to negative four point five eight per cent", "move blind -4.58%"),
    ("move blinds to negative three three point seventy-seven percent", "move blind -33.77%"),
    ("move blinds to negative eleven point three five one per cent", "move blind -11.351%"),
    # Duration
    ("move blinds to ten point eleven percent for 21 minutes", "move blind 10.11% 21m"),
    ("move blinds to minus ninety-nine point three four eight per cent for 4 hours", "move blind -99.348% 4h")
])
def test_voice_parser(input_line, expected):
    result = VoiceParser.parse(input_line)
    assert result == expected
