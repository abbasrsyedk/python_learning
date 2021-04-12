#
#
#

class Account():

    #owner balance deposit withdraw
    
    def __init__(self,owner,balance,deposit,withdraw):
        
        self.owner = owner
        self.balance = balance
        self.deposit = deposit
        self.withdraw = withdraw

    
    def Owner(self):

        owner = self.owner
        print(owner)

    def Balance(self):

        balance = self.balance
        print(balance)

    def Deposit(self,deposit):
        deposit = self.deposit
        self.balance = self.balance + self.deposit
        print("The amount deposited is " + self.deposit + "Now the total balance is " + self.balance)

        return deposit

    def Withdraw(self,withdraw):
        
        if self.withdraw < self.balance:
            
            withdraw = self.withdraw
            print("The amount withdraw is " + self.withdraw + "Now the total balance is " + self.balance)

        else:
            
            print("your balance is not sufficient.")
        
        return withdraw

    def __str__(self):
        return "owner :" +  self.owner + "\nbalance :" + self.balance


a = Account("Abbas",500,100,700)

print(a.Balance())
print(a.Owner())
print(a.Withdraw())
print(a.Deposit())

print(a.Balance())