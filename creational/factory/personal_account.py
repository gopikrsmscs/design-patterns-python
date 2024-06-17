from bank_account import BankAccount


class PersonalBankAccount(BankAccount):

    def __open_account__(self):
        print("Opened personal bank account")