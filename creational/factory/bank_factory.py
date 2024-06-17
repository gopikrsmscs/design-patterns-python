from business_account import BusinessAccount
from personal_account import PersonalBankAccount
from joint_account import JointBankAccount


class BankFactory:
    @staticmethod
    def __get_account__(type: str):
        if type == "personal":
            return PersonalBankAccount()
        elif type == "savings":
            return JointBankAccount()
        else:
            return BusinessAccount()


