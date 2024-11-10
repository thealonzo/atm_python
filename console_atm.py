from atm import *
from console_utils import *

EXIT_CODE = -1
MAX_TRIES = 3

class ConsoleATM(ATM):

    def __init__(self, account_manager:AccountManager):
        super().__init__(account_manager)
        self.connected_account = None


    def run_atm(self):
        self.account_manager.read_accounts()
        self.operate()


    def stop_atm(self):
        self.account_manager.write_accounts_changes()

    
    def _connect_to_atm(self, id_number:int) -> bool:
        accounts_for_id  = self.account_manager.get_accounts(id_number)
        if not accounts_for_id:
            print(f"Wrong ID number, id {id_number} doesn't exist")
            return False
        if len(accounts_for_id) > 1:
            print("Choose the account you want to connect to:")
            for account_id in accounts_for_id:
                print(account_id)
            chosen_account = get_id("")
            if chosen_account not in accounts_for_id:
                return False
        else:
            chosen_account = accounts_for_id[0]
        print(f"Bank account with id {chosen_account} was chosen")
        
        tries = 0
        while tries < MAX_TRIES:
            if self._connect_to_account(chosen_account, input("Please enter bank account password:")):
                return True
        return False
    

    def _connect_to_account(self, account_number:int, password:str) -> bool:
        if self.account_manager.connect(account_number, password):
            self.connected_account = account_number
            return True
        # else, connection failes
        return False


    def connect_to_atm(self) -> bool:
        id_number = get_id("Please enter your id number:")
        if id_number == INVALID_ACCOUNT:
            return False
        
        if id_number == EXIT_CODE:
            self.stop_atm()
            exit()

        return self._connect_to_atm(id_number)

    
    def check_balance(self):
        print(f"Your account balance is {self._check_balance(self.connected_account)}")


    def withdraw_money(self) -> bool:
        sum_to_withdraw = get_sum("withdraw")
        if sum_to_withdraw <= 0:
            return False
       
        balance = self._withdraw_money(self.connected_account, sum_to_withdraw)
        
        output("Withdrawal", balance)
        return True
    

    def deposit_money(self):
        sum_to_deposit = get_sum("deposit")
        if sum_to_deposit <= 0:
            return False
        
        balance = self._deposit_money(self.connected_account, sum_to_deposit)
        
        output("Deposit", balance)
        return True
    

    def change_password(self):
        new_password = input("Please enter the new password for your bank account:")
        self._change_password(self.connected_account, new_password)
        print("Password changed successfully")


    def transfer_money(self):
        account_deposit = get_id("Please enter the account you would like to transfer money to:")
        if account_deposit == INVALID_ACCOUNT or not self.account_manager.check_if_account_exists(account_deposit):
            print("The Bank account you wish to transfer money to doesn't exist")
            return False
        if account_deposit == self.connected_account:
            print("You can't transfer money to yourself")
            return False
        
        sum_to_transfer = get_sum("transfer")
        if sum_to_transfer <= 0:
            return False
        
        balance = self._transfer_money(self.connected_account, account_deposit, sum_to_transfer)
        output("Transfer", balance)
        return True


    def operate(self):
        if self.connected_account:
            action = input("\nPlease select the operation you would like to perform:\n1. Check account balance\n2. Withdraw cash\n3. Deposit cash\n4. Change account Password\n5. Transfer money to another account\n6. Exit your account\n\n")
            try:
                action = int(action)
            except ValueError:
                action = 0
            clear()
            match action:
                case 1:
                    self.check_balance()
                case 2:
                    self.withdraw_money()
                case 3:
                    self.deposit_money()
                case 4:
                    self.change_password()
                case 5:
                    self.transfer_money()
                case 6:
                    self.connected_account = None
                case default:
                    print("Invaild command chosen")
        else:
            self.connect_to_atm()
        self.operate()

