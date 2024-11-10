from atm import *
class ConsoleATM(ATM):

    def __init__(self, account_manager:AccountManager):
        super().__init__(account_manager)
        self.connected_account = None


    def run_atm(self):
        self.account_manager.read_accounts()
        self.operate()


    def stop_atm(self):
        self.account_manager.write_accounts_changes()

    
    def _connect_to_atm(self, id_number):
        accounts_for_id  = self.account_manager.get_accounts(id_number)
        if not accounts_for_id:
            print(f"Wrong ID number, id {id_number} doesn't exist")
            return False
        
        print("Choose the account you want to connect to:")
        for account_id in accounts_for_id:
            print(account_id)
        chosen_account = int(input())
        if chosen_account not in accounts_for_id:
            return False
        print(f"Bank account with id {chosen_account} was chosen")
        
        tries = 0
        while tries < 3:
            if self._connect_to_account(chosen_account, input("Please enter bank account password:")):
                return True
        return False
    

    def _connect_to_account(self, account_number, password):
        if self.account_manager.connect(account_number, password):
            self.connected_account = account_number
            return True
        # else, connection failes
        return False


    def connect_to_atm(self):
        id_number = input("Please enter your id number:")
        if id_number == "-1":
            self.stop_atm()
            exit()
        try:
            id_number = int(id_number)
            return self._connect_to_atm(id_number)
        except:
            return False

    
    def check_balance(self):
        print(f"Your account balance is {self._check_balance(self.connected_account)}")


    def check_sum(sum):
        try:
            sum = float(sum)
            return sum
        except:
            return -1


    def withdraw_money(self):
        sum_to_withdraw = ConsoleATM.check_sum(input("Please enter the sum you would like to withdraw:"))
        if sum_to_withdraw <= 0:
            print("Can't withdraw non positive amount of money")
            return False
       
        withdrawal = self._withdraw_money(self.connected_account, sum_to_withdraw)
        if withdrawal:
            print("Money withdrawal was successful")
            return True
        else:
            print("Money withdrawal failed, account balance is too low")
            return False
    

    def deposit_money(self):
        sum_to_deposit = ConsoleATM.check_sum(input("Please insert the cash you would like to deposit:"))
        if sum_to_deposit <= 0:
            print("Can't deposit non positive amount of money")
            return False
        
        self._deposit_money(self.connected_account, sum_to_deposit)
        print("Money deposit was successful")
        return True
    

    def change_password(self):
        new_password = input("Please enter the new password for your bank account:")
        if self._change_password(self.connected_account, new_password):
            print("Password changed successfully")
            return True
        else:
            print("Password didn't change, this is your current password")
            return False


    def transfer_money(self):
        account_deposit = input("Please enter the account you would like to transfer money to:")
        invalid_account = False
        try:
            account_deposit = int(account_deposit)
        except:
            invalid_account = True
        if invalid_account or not self.account_manager.check_if_account_exists(account_deposit):
            print("The Bank account you wish to transfer money to doesn't exist")
            return False
        sum_to_transfer = ConsoleATM.check_sum(input(f"Please enter the sum you would like to transfer from your bank account to bank account {account_deposit}:"))
        
        if sum_to_transfer <= 0:
            print("Can't withdraw non positive amount of money")
            return False
        self._transfer_money(self.connected_account, account_deposit, sum_to_transfer)
        return True


    def operate(self):
        if self.connected_account:
            action = int(input("Please select the operation you would like to perform:\n1. Check account balance\n2. Withdraw cash\n3. Deposit cash\n4. Change account Password\n5. Transfer money to another account\n6. Exit your account\n"))
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