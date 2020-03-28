"""
Date: Mar 27, 2020
Author: Ishaat Chowdhury
Contents: Defines base class for voice command
"""
from abc import ABCMeta, abstractmethod, abstractclassmethod
from rpi_voice_control.constants import DEFAULT_RPI_SERVER_IP, DEFAULT_RPI_SERVER_PORT

""" Base class for voice command. Sends commands to RPI server.
"""
class Command(metaclass=ABCMeta):

    """ Constructs command object

    Arguments:
        ip {str} - ip address of RPI server
        port {int} - port of RPI server
    """
    def __init__(self, ip=DEFAULT_RPI_SERVER_IP, port=DEFAULT_RPI_SERVER_PORT):
        self._ip = ip
        self._port = port

    """ Determines if another object instance is equal to this object instance

    Arguments:
        other {object} - other object to compare
    """
    def __eq__(self, other):
        if isinstance(other, Command):
            return self._ip == other._ip and self._port == other._port
        return False

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
    def build(cls, text, **kwargs):
        raise NotImplementedError 
