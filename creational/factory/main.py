from bank_factory import BankFactory
if __name__ == "__main__":
    account = input("Enter account type (business/savings/personal): ").lower()
    bank = BankFactory.__get_account__(type=account)
    print(bank.__open_account__())
