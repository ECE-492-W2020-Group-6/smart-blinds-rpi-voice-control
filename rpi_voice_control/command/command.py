from abc import ABCMeta, abstractmethod, abstractclassmethod

class Command(metaclass=ABCMeta):

    @abstractmethod 
    def __str__(self):
        raise NotImplementedError

    @abstractmethod
    def run(self):
        raise NotImplementedError

    @abstractclassmethod
    def build(cls, text):
        raise NotImplementedError 

class CommandFactory():

    @staticmethod
    def build(text):
        for subclass in Command.__subclasses__():
            command = subclass.build(text) 
            if command is not None:
                return command

        return None
            
