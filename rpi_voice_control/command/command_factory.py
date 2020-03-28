from rpi_voice_control.command.command import Command
from rpi_voice_control.command.position import PositionCommand

class CommandFactory():

    @staticmethod
    def build(text):
        Command.register(PositionCommand)
        for subclass in Command.__subclasses__():
            command = subclass.build(text) 
            if command is not None:
                return command

        return None
