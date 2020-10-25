from Bank import BankAccount, BankUser, AccountType


def test_over_withdrawal():
    # Test with SAVINGS account
    user = BankUser('Joe')
    user.addAccount(AccountType.SAVINGS)
    user.deposit(AccountType.SAVINGS, 10)
    print(f'Balance for SAVINGS account is {user.getBalance(AccountType.SAVINGS)}')
    print(str(user))

    # Withdraw more money than balance
    try:
        user.withdraw(AccountType.SAVINGS, 1000)
    except Exception as e:
        print(e)

    # Withdraw negative amount
    try:
        user.withdraw(AccountType.SAVINGS, -10)
    except Exception as e:
        print(e)

    # Deposit negative amount
    try:
        user.deposit(AccountType.SAVINGS, -20)
    except Exception as e:
        print(e)

    # Add two SAVINGS account
    try:
        user.addAccount(AccountType.SAVINGS)
    except Exception as e:
        print(e)

    # Get balance from account that does not exist
    try:
        user.getBalance(AccountType.CHECKING)
    except Exception as e:
        print(e)

    # Deposit to account that does not exist
    try:
        user.deposit(AccountType.CHECKING, 10)
    except Exception as e:
        print(e)

    # Withdraw to account that does not exist
    try:
        user.withdraw(AccountType.CHECKING, 20)
    except Exception as e:
        print(e)

    # Test with CHECKING account
    user.addAccount(AccountType.CHECKING)
    user.deposit(AccountType.CHECKING, 100)
    user.withdraw(AccountType.CHECKING, 50)
    print(f'Balance for CHECKING account is {user.getBalance(AccountType.CHECKING)}')
    print(str(user))


test_over_withdrawal()
