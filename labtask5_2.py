class BankAccount:
    def __init__(self,__account_holder, __balance=0):#constructor
        self.__account_holder=__account_holder #private variable
        self.__balance=__balance#private variable
    #getter and setter for account holder
    def get_account_holder(self):
        return self.__account_holder
    def set_account_holder(self, __account_holder):
        self.__account_holder=__account_holder
    #getter and setter for balance
    def get_balance(self):
        return self.__balance
    def set_balance(self, balance):
        if balance>=0:
            self.__balance=balance
        else:
            print("Balance cannot be negative")
#object creation
account= BankAccount("Kinza")

account.set_account_holder("Kinza")
account.set_balance(5000)
print("Account Holder:", account.get_account_holder())
print("Account Balance:", account.get_balance())

account.set_balance(-1000) #attempting to set negative balance
print("Account Balance:", account.get_balance()) #check balance after setting negative value