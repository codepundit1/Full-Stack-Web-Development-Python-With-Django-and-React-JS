""" custom exception"""

class SmallNumberException(Exception):
    def __init__(self, message="number is smaller than 10"):
        self.message = message
        super().__init__(self.message)

class BigNumberException(Exception):
    def __init__(self, message="number is bigget than 100"):
        self.message = message
        super().__init__(self.message)
class NumeberNotInRange(Exception):
    def __init__(self, number, message = ""):
        self.number = number
        self.message = str(number) +" "+ "is not in range"
        super().__init__(self.message)    

class Number():
    def takeNumber(self, Number):
        try:
            if Number < 10:
                raise SmallNumberException
            if Number > 100:
                raise BigNumberException

            print(Number)
        except SmallNumberException as e:
            print(e)
        except BigNumberException as e:
            print(e)
    
    def number2(self, number):
        try:
            if not 100 < number < 200:
                raise NumeberNotInRange(number)
            print(number, "is perfect in range")
        except NumeberNotInRange as e:
            print(e)
        

number = Number()
number.takeNumber(58)
number.number2(102)