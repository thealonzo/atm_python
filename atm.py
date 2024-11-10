from abc import ABC, abstractmethod


class AccountManager(ABC):

    @abstractmethod
    def connect(self, account_number:int, account_pass:str) -> bool:
        pass


    @abstractmethod
    def read_accounts(self):
        pass


    @abstractmethod
    def write_accounts_changes(self):
        pass

    
    @abstractmethod
    def get_account_balance(self, account_number:int) -> float:
        pass


    @abstractmethod
    def deposit_money(self, account_number:int, sum:float) -> bool:
        pass


    @abstractmethod
    def withdraw_money(self, account_number:int, sum:float) -> bool:
        pass


    @abstractmethod
    def change_password(self, account_number:int, new_password:str) -> str:
        pass


    @abstractmethod
    def get_accounts(self, id_number:int) -> list[int]:
        pass


    @abstractmethod
    def check_if_account_exists(self, account_number:int) -> bool:
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
    def _connect_to_atm(self, id_number:int) -> bool:
        pass

    
    @abstractmethod
    def _connect_to_account(self, account_number:int, password:str) -> bool:
        pass


    def _check_balance(self, account_number:int) -> float:
        return self.account_manager.get_account_balance(account_number)


    def _withdraw_money(self, account_number:int, sum:float) -> float:
        return self.account_manager.withdraw_money(account_number, sum)
    

    def _deposit_money(self, account_number: int, sum: float) -> float:
        return self.account_manager.deposit_money(account_number, sum)
    

    def _change_password(self, account_number:int, new_password:str) -> str:
        return self.account_manager.change_password(account_number, new_password)
    

    def _transfer_money(self, account_withdraw:int, account_deposit:int, sum:float) -> bool:
        balance = self._withdraw_money(account_withdraw, sum):
        self._deposit_money(account_deposit, sum)
        return balance