"""
Date: Mar 27, 2020
Author: Ishaat Chowdhury
Contents: Defines inteface for voice command
"""
from abc import ABCMeta, abstractmethod, abstractclassmethod

""" Interface for voice command
"""
class Command(metaclass=ABCMeta):

    """ Convert command to str
    """
    @abstractmethod 
    def __str__(self):
        raise NotImplementedError

    """ Run command

    Usually, the command object will make an API request to the RPI Smart Blinds Server
    """
    @abstractmethod
    def run(self):
        raise NotImplementedError

    """ Builder method to build instance of class from parsed voice command (as text)

    Returns:
        an instance of Command or None
    """
    @abstractclassmethod
    def build(cls, text):
        raise NotImplementedError 
