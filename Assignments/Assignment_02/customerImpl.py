from customer import Customer

class CustomerImpl(Customer):



    def __init__(self, name, accountNumber):
        self.name = name
        self.accountNumber = accountNumber

    
    def getName(self):
        return self.name
        
    def setName(self, name):
        self.name = name

    
    def getAccountNumber(self):
        return self.accountNumber
    
    def setAccountNumber(self, accountNumebr):
        self.accountNumber = accountNumebr


customer = CustomerImpl("MD. Jahid Hasan", 101)
print("Customer Name: ", customer.name,", " "Bank Account Number:", customer.accountNumber)