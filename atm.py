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
    def get_account_balance(self, account_number):
        pass


    @abstractmethod
    def deposit_money(self, account_number, sum):
        pass


    @abstractmethod
    def withdraw_money(self, account_number, sum):
        pass


    @abstractmethod
    def change_password(self, account_number, new_password):
        pass


    @abstractmethod
    def get_accounts(self, id_number):
        pass


    @abstractmethod
    def check_if_account_exists(self, account_number):
        pass


class ATM(ABC):
    def __init__(self, account_manager:AccountManager):
        self.account_manager = account_manager


    @abstractmethod
    def run_atm(self):
        pass


    @abstractmethod
    def stop_atm(self):
        pass

    
    @abstractmethod
    def _connect_to_atm(self, id_number):
        pass

    
    @abstractmethod
    def _connect_to_account(self, account_number, password):
        pass


    def _check_balance(self, account_number):
        return self.account_manager.get_account_balance(account_number)


    def _withdraw_money(self, account_number, sum):
        return self.account_manager.withdraw_money(account_number, sum)
    

    def _deposit_money(self, account_number, sum):
        return self.account_manager.deposit_money(account_number, sum)
    

    def _change_password(self, account_number, new_password):
        return self.account_manager.change_password(account_number, new_password)
    

    def _transfer_money(self, account_withdraw, account_deposit, sum):
        if not self._withdraw_money(account_withdraw, sum):
            return False
        self._deposit_money(account_deposit, sum)
        return True