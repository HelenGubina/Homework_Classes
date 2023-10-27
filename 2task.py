class BankAccount:
    def __init__(self, owner, number, balance):
        self.owner = owner
        self.number = number
        self.balance = balance

    def with_draw(self, trans_sum):
        self.balance = self.balance-trans_sum

    def top_up(self, trans_sum):
        self.balance = self.balance+trans_sum

    def __str__(self):
        return "Your balance is:  " + str(self.balance)


acc1 = BankAccount("Морар Василь Петрович", "UA309445528000098293948475670", 50000)
acc1.with_draw(2000)
print(acc1)
acc1.top_up(10000)
print(acc1)
