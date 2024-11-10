from abc import ABC, abstractmethod


class AccountManager(ABC):

    @abstractmethod
    def connect(self, account_number, account_pass):
        pass


    @abstractmethod
    def read_accounts(self):
        pass


    @abstractmethod
    def write_accounts_changes(self):
        pass


    @abstractmethod
    def deposit_money(self, account_number):
        pass


    @abstractmethod
    def withdraw_money(self, account_number):
        pass
