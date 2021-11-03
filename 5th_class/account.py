from student_impl import StudentImpl

class Account(StudentImpl):


    def __init__(self, name, dept, credit, amount, weaver = 0):
        super(Account, self).__init__(name=name, dept=dept)
        self.credit = credit
        self.amount = amount
        self.weaver = weaver
        self.payment = 0.0

    def get_total_sem_fees(self):
        return self.credit * self.amount
    
    def get_payment_amount_without_weaver(self):
        if self.weaver == 0:
            self.payment = self.credit * self.amount
            return "You have no weaver" + self.payment
        else:
            self.payment = (self.credit * self.amount) - self.weaver
            return self.payment
        
    
    def make_payment(self, amount):
         self.payment = self.payment - amount
         return self.payment


account=Account("Abir", "ENG", 20, 5000, 25000)
print(account.getName())
print(account.getDept())
print("Total paidable amount :")
print(account.get_total_sem_fees())
print("After getting weaver or not amount :")
print(account.get_payment_amount_without_weaver())
print("Due is :")
print(account.make_payment(25000))
print("Due is :")
print(account.make_payment(20000))
