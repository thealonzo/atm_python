from atm import *
class ConsoleATM(ATM):

    def __init__(self, account_manager:AccountManager):
        super().__init__(account_manager)
        self.connected_account = None


    def run_atm(self):
        self.account_manager.read_accounts()


    def stop_atm(self):
        self.account_manager.write_accounts_changes()

    
    def connect_to_atm(self, id_number):
        accounts_for_id  = self.account_manager.get_accounts(id_number)
        if not accounts_for_id:
            print(f"Wrong ID number, id {id_number} doesn't exist")
            return None
        print("Choose the account you want to connect to:")
        for index in range(len(accounts_for_id)):
            print(index, accounts_for_id[index])
        chosen_account = int(input())
        if chosen_account not in range(len(accounts_for_id)):
            return False
        print(f"Bank account with id {accounts_for_id[chosen_account]} was chosen")
        tries = 0
        while tries < 3:
            if self.connect_to_account(accounts_for_id[chosen_account], input("Please enter bank account password:")):
                return True
        return False
    

    def connect_to_account(self, account_number, password):
        if self.account_manager.connect(account_number, password):
            self.connected_account = account_number
            return True
        # else, connection failes
        return False


    def connect_to_atm(self):
        id_number = input("Please enter your id number:")
        return self.connect_to_atm(id_number)

    
    def check_balance(self):
        print(self.account_manager.get_account_balance(self.connected_account))


    def check_sum(sum):
        try:
            sum = float(sum)
            return sum
        except:
            return -1
    # def withdraw_money(self, account_number, sum):
    #     return self.account_manager.withdraw_money(account_number, sum)
    


    def withdraw_money(self):
        sum_to_withdraw = ConsoleATM.check_sum(input("Please enter the sum you would like to withdraw:"))
        if sum_to_withdraw <= 0:
            print("Can't withdraw non positive amount of money")
            return False
        withdrawal = self.withdraw_money(self.connected_account, sum_to_withdraw)
        if withdrawal:
            print("Money withdrawal was successful")
            return True
        else:
            print("Money withdrawal failed, account balance is too low")
            return False
        

    # def deposit_money(self, account_number, sum):
    #     return self.account_manager.deposit_money(account_number, sum)
    

    def deposit_money(self):
        sum_to_deposit = ConsoleATM.check_sum(input("Please insert the cash you would like to deposit:"))
        if sum_to_deposit <= 0:
            print("Can't deposit non positive amount of money")
            return False
        self.deposit_money(self.connected_account, sum_to_deposit)
        print("Money deposit was successful")
        return True


    # def change_password(self, account_number, new_password):
    #     return self.account_manager.change_password(account_number, new_password)
    

    def change_password(self):
        new_password = input("Please enter the new password for your bank account:")
        if self.change_password(self.connected_account, new_password):
            print("Password changed successfully")
            return True
        else:
            print("Password didn't change, this is your current password")
            return False
        

    # def transfer_money(self, account_withdraw, account_deposit, sum):
    #     self.withdraw_money(account_withdraw, sum)
    #     self.deposit_money(account_deposit, sum)


    def transfer_money(self):
        account_deposit = input("Please enter the account you would like to transfer money to:")
        if not self.account_manager.check_if_account_exists(account_deposit):
            print("The Bank account you wish to transfer money to doesn't exist")
            return False
        sum_to_transfer = ConsoleATM.check_sum(input(f"Please enter the sum you would like to transfer from your bank account to bank account {account_deposit}:"))
        if sum_to_transfer <= 0:
            print("Can't withdraw non positive amount of money")
            return False
        self.transfer_money(self.connected_account, account_deposit, sum_to_transfer)
        return True


    def operate(self):
        if self.connected_account:
            action = int(input("Please select the operation you would like to perform:\n1. Check account balance\n2. Withdraw cash\n3. Deposit cash\n4.Change account Password\n5.Transfer money to another account\n6. Exit your account\n"))
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