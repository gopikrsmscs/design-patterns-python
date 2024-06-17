from bank_account import BankAccount


class BusinessAccount(BankAccount):

    def __open_account__(self):
        print("Opening Business Account")
