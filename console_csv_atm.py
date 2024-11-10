from console_atm import *
from csv_manager import *
def main():
    csv_manager = CSV_AccountManager("accounts.csv")
    console_csv_atm = ConsoleATM(csv_manager)
    console_csv_atm.run_atm()


if __name__ == "__main__":
    main()