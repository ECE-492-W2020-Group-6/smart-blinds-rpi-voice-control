"""
Date: Mar 27, 2020
Author: Ishaat Chowdhury
Contents: Factory class for creating instances of Command subclass
"""
from rpi_voice_control.command.command import Command
from rpi_voice_control.command.position import PositionCommand

""" Factory object that builds subclasses of Command
"""
class CommandFactory():

    """ Factory method to instantiate instances of subclass of Command
        based on input text

    Arguments:
        text {str} - text representation of voice command
        kwargs {dict} - other optional parameters to pass to superclass

    Returns:
        an instance of a subclass of Command or None
    """
    @staticmethod
    def build(text, **kwargs):
        # Register subclass
        # Have to do this explicitly since Python only registers
        # subclasses upon import
        Command.register(PositionCommand)

        # See if a valid command subclass can be created from the text
        # and return that subclass instance 
        for subclass in Command.__subclasses__():
            command = subclass.build(text, **kwargs) 
            if command is not None:
                return command

        return None
