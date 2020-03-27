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

class VoiceParser():
    # Class variables
    TEXT2D = Text2Digits()
    DECIMAL_PATTERN = re.compile(r"(?:(\d+)\s*point\s*(\d+))")
    NEGATIVE_PATTERN = re.compile(r"(?:(?:minus|negative)\s*(\d+(?:\.\d+)*))")
    STEMMER = PorterStemmer()

    @classmethod
    def parse(cls, line):
        # Replace substrings with number as word to digits
        # Ex. "move blinds to minus fifty-seven point one one three" 
        #       -> "move blinds to minus 57 point 113 percent"
        result = cls.TEXT2D.convert(line)

        # Replace substrings with integers around word "point" with decimal representation
        # Ex. "move blinds to minus 57 point 113 percent" 
        #       -> "move blinds to minus 57.113 percent"
        result = cls.DECIMAL_PATTERN.sub(r"\g<1>.\g<2>", result)

        # Replace substrings with "minus"/"negative" preceding integer/decimal with -integer/decimal
        # Ex. "move blinds to minus 57.113 percent" -> "move blinds to -57.113 percent"
        result = cls.NEGATIVE_PATTERN.sub(r"-\g<1>", result)

        # Stem words
        # Ex. "move blinds to -57.113 percent" -> "move blind to -57.113 percent"
        result = " ".join(map(cls.STEMMER.stem, result.split()))

        # Remove stop words (ex. to, is, not)
        # Ex. "move blind to -57.113 percent" -> "move blind -57.113 percent"
        result = " ".join(filter(lambda w: w not in stopwords.words(), result.split()))

        return result
