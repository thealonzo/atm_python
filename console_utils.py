import os

INVALID_ACCOUNT = -2
INVALID_SUM = -1


def clear():
    os.system('cls')


def get_sum(request: str) -> float:
    sum = input(f"Please enter the sum you would like to {request}:")
    try:
        sum = float(sum)
    except ValueError:
        sum = INVALID_SUM
    if sum <= 0:
        print(f"Can't {request} non positive amount of money")
    return sum


def get_id(request: str) -> int:
    id = input(request)
    try:
        id = int(id)
    except ValueError:
        id = INVALID_ACCOUNT
    return id


def output(operation: str, balance: float):
    print(f"\n{operation} was successful, account balance is {balance}")
