"""
Date: Mar 27, 2020
Author: Ishaat Chowdhury
Contents: Contains class that parses voice input
"""

from text2digits.text2digits import Text2Digits
import re
from nltk import download
from nltk.stem import PorterStemmer
from nltk.corpus import stopwords
download("stopwords")

""" Class that parses raw voice command into usable text
"""
class VoiceParser():
    # Class variables
    TEXT2D = Text2Digits()
    DECIMAL_PATTERN = re.compile(r"(?:(\d+)\s*point\s*(\d+))")
    NEGATIVE_PATTERN = re.compile(r"(?:(?:minus|negative)\s*(\d+(?:\.\d+)?))")
    PERCENT_PATTERN = re.compile(r"(?:(-?\d+(?:\.\d+)?)\s*per\s*cent)")
    DURATION_PATTERN_MINUTES = re.compile(r"(?:(\d+)\s*minutes?)")
    DURATION_PATTERN_HOURS = re.compile(r"(?:(\d+)\s*hours?)")
    STEMMER = PorterStemmer()

    """ Class method that parses single line of text

    Arguments:
        line {str} - line of voice command

    Returns:
        result {str} - parsed line
    """
    @classmethod
    def parse(cls, line):
        # Replace substrings with number as word to digits
        result = cls.TEXT2D.convert(line)

        # Replace substrings with integers around word "point" with decimal representation
        result = cls.DECIMAL_PATTERN.sub(r"\g<1>.\g<2>", result)

        # Replace substrings with "minus"/"negative" preceding integer/decimal with -integer/decimal
        result = cls.NEGATIVE_PATTERN.sub(r"-\g<1>", result)

        # Replace number "percent" with number%
        result = cls.PERCENT_PATTERN.sub(r"\g<1>%", result)

        # Replace number followed by "minutes" or "hours" into encoded duration
        result = cls.DURATION_PATTERN_MINUTES.sub(r"\g<1>m", result)
        result = cls.DURATION_PATTERN_HOURS.sub(r"\g<1>h", result)

        # Stem words
        result = " ".join(map(cls.STEMMER.stem, result.split()))

        # Remove stop words (ex. to, is, not)
        result = " ".join(filter(lambda w: w not in stopwords.words(), result.split()))

        return result
