from abc import ABC, abstractmethod


class BankAccount(ABC):
    @abstractmethod
    def __open_account__(self):
        pass
