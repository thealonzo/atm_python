from console_atm import *
from csv_manager import *
def main():
    csv_manager = CSV_AccountManager("accounts.csv")
    # csv_manager.read_accounts()
    # print(csv_manager.accounts)
    console_csv_atm = ConsoleATM(csv_manager)
    console_csv_atm.run_atm()


if __name__ == "__main__":
    main()