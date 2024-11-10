import pandas as pd
from atm import AccountManager
class CSV_AccountManager(AccountManager):
    
    def __init__(self, csv_path:str):
        self.csv_path = csv_path
        self.accounts = None
        

    def connect(self, account_number:int, account_pass:str) -> bool:
        account = self.accounts[self.accounts["account_number"] == account_number]["atm_code"].tolist()
        if account:
            if account[0] == account_pass:
                return True
        return False


    def read_accounts(self):
        self.accounts = pd.read_csv(self.csv_path, dtype={"account_number": "int64", "id_number": "int64", "name": "string", "balance": "float64", "atm_code": "string"})


    def write_accounts_changes(self):
        self.accounts.to_csv(self.csv_path, index=False)

    
    def get_account_balance(self, account_number:int) -> float:
        return self.accounts[self.accounts["account_number"] == account_number]["balance"].tolist()[0]


    def deposit_money(self, account_number:int, sum:float) -> bool:
        self.accounts.loc[self.accounts["account_number"] == account_number, "balance"] += sum
        return self.get_account_balance(account_number)


    def withdraw_money(self, account_number:int, sum:float) -> bool:
        self.accounts.loc[self.accounts["account_number"] == account_number, "balance"] -= sum
        return self.get_account_balance(account_number)


    def change_password(self, account_number:int, new_password:str) -> bool:
        self.accounts.loc[self.accounts["account_number"] == account_number, "atm_code"] = new_password
        return True


    def get_accounts(self, id_number:int) -> list[int]:
        return self.accounts[self.accounts["id_number"] == id_number]["account_number"].tolist()


    def check_if_account_exists(self, account_number:int) -> bool:
        return account_number in self.accounts["account_number"].tolist()

