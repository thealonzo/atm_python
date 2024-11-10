import pandas as pd
from atm import AccountManager
class CSV_AccountManager(AccountManager):
    
    def __init__(self, csv_path):
        self.csv_path = csv_path
        self.accounts = None
        

    def connect(self, account_number, account_pass):
        account = self.accounts[self.accounts["account_number"] == account_number]["atm_code"].tolist()
        if account:
            if account[0] == account_pass:
                return True
        return False


    def read_accounts(self):
        self.accounts = pd.read_csv(self.csv_path)


    def write_accounts_changes(self):
        self.accounts.to_csv(self.csv_path)

    
    def get_account_balance(self, account_number):
        return self.accounts[self.accounts["account_number"] == account_number]["balance"].tolist()[0]


    def deposit_money(self, account_number, sum):
        self.accounts.loc[self.accounts["account_number"] == account_number, "balance"] += sum
        return True


    def withdraw_money(self, account_number, sum):
        if self.get_account_balance(account_number) < sum:
            return False
        self.accounts.loc[self.accounts["account_number"] == account_number, "balance"] -= sum
        return True

    def change_password(self, account_number, new_password):
        self.accounts.loc[self.accounts["account_number"] == account_number, "atm_code"] = new_password
        return True


    def get_accounts(self, id_number):
        self.accounts[self.accounts["id_number"] == id_number]["account_number"].tolist()


    def check_if_account_exists(self, account_number):
        return account_number in self.accounts["account_number"]

