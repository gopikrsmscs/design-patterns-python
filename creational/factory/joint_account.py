from bank_account import BankAccount


class JointBankAccount(BankAccount):

    def __open_account__(self):
        print("Open savings bank")
