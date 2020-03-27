from text2digits.text2digits import Text2Digits
import re
from nltk.stem import PorterStemmer

class VoiceParser():
    # Class variables
    TEXT2D = Text2Digits()
    DECIMAL_PATTERN = re.compile(r"(?:(\d+)\s*point\s*(\d+))")
    NEGATIVE_PATTERN = re.compile(r"(?:(?:minus|negative)\s*(\d+(?:\.\d+)*))")
    STEMMER = PorterStemmer()

    @classmethod
    def parse(cls, line):
        # Replace substrings with number as word to digits
        # Ex. "one hundred" -> "100"
        result = cls.TEXT2D.convert(line)
        # Replace substrings with integers around word "point" with decimal representation
        # Ex. "five point 7" -> "5.7" 
        result = cls.DECIMAL_PATTERN.sub(r"\g<1>.\g<2>", result)
        # Replace substrings with "minus"/"negative" preceding integer/decimal with -integer/decimal
        # Ex. "minus 13.159" -> "-13.159"
        result = cls.NEGATIVE_PATTERN.sub(r"-\g<1>", result)
        # Stem words
        result = " ".join(map(cls.STEMMER.stem, result.split()))
        return result
