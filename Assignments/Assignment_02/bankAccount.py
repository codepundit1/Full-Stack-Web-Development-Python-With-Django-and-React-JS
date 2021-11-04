from customer import Customer
from customerImpl import CustomerImpl

class BankAccount(CustomerImpl):

    def __init__(self, name, accountNumber, depopsit, withdraw, initial_balance = 500):
        super(BankAccount, self).__init__(name=name, accountNumber=accountNumber)
        self.deposit = depopsit
        self.withdraw = withdraw
        self.initial_balance =initial_balance
        self.amount = 0.0
    
    def get_total_balance(self):
        return self.initial_balance
        
    def get_deposit_amount(self):
        self.amount = self.initial_balance + self.deposit
        return self.amount

    def get_withdraw_amount(self):
        self.amount = (self.initial_balance + self.deposit) - self.withdraw
        return self.amount

    def get_amount_without_withdraw(self):
        if self.withdraw == 0:
            self.amount = self.initial_balance + self.deposit
            return self.amount
        else:
            self.amount = (self.initial_balance + self.deposit) - self.withdraw
            return self.amount


bankAccount = BankAccount('Mr. Tom', 102, 1000, 50 , 500)
print("Name: ", bankAccount.getName())
print("Account Number: ",bankAccount.getAccountNumber())
print("Opening Balance: ",bankAccount.get_total_balance())
print("After deposit Total Balance: ", bankAccount.get_deposit_amount())
print("After withdraw Total Balance: ", bankAccount.get_withdraw_amount())
print("Total Bank Balance: ", bankAccount.get_amount_without_withdraw())