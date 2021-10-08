# Abstraction
from abc import ABC, abstractmethod, abstractproperty

class Student(ABC):

    @abstractmethod
    def getName(self):
        pass

    @abstractmethod
    def setName():
        pass
    
    @abstractmethod
    def getDept():
        pass
    
    @abstractmethod
    def setDept():
        pass