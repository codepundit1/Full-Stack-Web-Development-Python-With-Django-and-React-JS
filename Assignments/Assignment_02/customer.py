from abc import ABC, abstractmethod, abstractproperty

class Customer(ABC):
    


    @abstractmethod
    def getName(self):
        pass

    @abstractmethod
    def setName(self, name):
        pass

    @abstractmethod
    def getAccountNumber(self):
        pass

    @abstractmethod
    def setAccountNumber(self, accountNumebr):
        pass