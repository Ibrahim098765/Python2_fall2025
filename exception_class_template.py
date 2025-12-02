# Work on exception class to handle customized exceptions

class BankAccount:
    """ Bank Account class to keep track banking activities """

    def __init__(self, name, balance=0):
        """ Initialize the account holder's name and starting balance """
        pass
    # getters and setters   
    def get_name(self):
        """ Return the account holder's name """
        pass 
    def set_name(self,name):
        """ Set the account holder's name """
        pass 
    def get_balance(self):
        """ Return the current balance """
        pass 
    def set_balance(self,balance):
        """ Set the current balance """
        pass
    
    # methods
    def deposit(self, amount):
        """ Deposit money into the account """
        pass    
    def withdraw(self, amount):   
        """ Withdraw money from the account """
        pass           
    def __str__(self):
        """ Return a string representation of the account """
        return f'Account holder: {self.__name}, Balance: ${self.__balance:.2f}'

# exception class
class NegativeException(Exception):
    """ Custom exception for negative values """
    def __init__(self, message):
        """ initializer """
        
     
def main():
    try: 
        # create a bank account
        jsmith_account = BankAccount("John Smith", 100)
        print(jsmith_account)

        # deposit money
        jsmith_account.deposit(50)
        print("After depositing $50:", jsmith_account)

        # withdraw money
        jsmith_account.withdraw(30)
        print("After withdrawing $30:", jsmith_account)

        # attempt to withdraw more than the balance
        jsmith_account.withdraw(150)

    except NegativeException as ne:
        print(ne)
    except Exception as ex:
        print("An unexpected error occurred:", ex)   

main()
    