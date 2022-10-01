import uuid

'''
Banking application class list:
1. user
2. account
3. transaction

'''

class User:
    def __init__(self, first_name, last_name):
        self.__f_name = first_name
        self.__l_name = last_name
        self.__user_id = uuid.uuid4()
        self.__accounts = []

    def get_first_name(self):
        return self.__f_name
    
    def get_last_name(self):
        return self.__l_name
    
    def get_user_id(self):
        return self.__user_id

    def set_first_name(self, first_name):
        self.__f_name = first_name
    
    def set_last_name(self, last_name):
        self.__l_name = last_name

    def add_account(self, account_id):
        self.__accounts.append(account_id)


class Account:
    def __init__(self):
        self.__account_id = uuid.uuid4()
        self.__balance = 0
        self.__owners = []
        self.__transactions = []
    
    def get_account_id(self):
        return self.__account_id

    def get_balance(self):
        return self.__balance
    
    def add_owner(self, user_id):
        self.__owners.append(user_id)

    def deposit(self, amount):
        self.__balance += amount
        tr = Transaction(amount, "deposit", self.__account_id)
        self.__transactions.append(tr)

    def withdraw(self, amount):
        self.__balance -= amount

class Transaction:
    def __init__(self, amount, tr_type, orig_acct, dest_account=""):
        self.__amount = amount
        self.__tr_type = tr_type
        self.__orig_acct = orig_acct
        self.__dest_account = dest_account
        self.__transaction_id = uuid.uuid4()

    def get_amount(self):
        return self.__amount

    

user = User("Dmitriy", "Babichenko")
print(user.get_user_id())

account = Account()
print("Init balance: ", account.get_balance())
account.add_owner(user.get_user_id())
account.deposit(1000)
print("Balance after deposit: ", account.get_balance())