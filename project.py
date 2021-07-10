class ATM(object):
    def __init__(self, cardNumber, pin):
        self.cardNumber = cardNumber
        self.pin = pin
        self.balance = 50000
    
    def withdrawal(self, amount):
        print("Amount ", amount, " has been withdrawn.")
        self.balance = self.balance - amount
        print("remaining balance is ", self.balance)

    def deposit(self, amount):
        self.balance = self.balance + amount
        print("New balance is ", self.balance)

cardNumber = input("Please input your card number: ")
pin = input("Please input your pin: ")
atm = ATM(cardNumber, pin)
option = input("Please enter 1 for withdrawal and 2 for deposit: ")

if option == "1":
    amount = int(input("Please write the amount you want to withdraw: "))
    atm.withdrawal(amount)
else:
    amount = int(input("Please write the amount you want to deposit: "))
    atm.deposit(amount)
