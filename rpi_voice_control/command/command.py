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
