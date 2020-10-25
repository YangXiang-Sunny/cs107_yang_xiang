from enum import Enum


class AccountType(Enum):
    SAVINGS = 1
    CHECKING = 2


class BankAccount():

    def __init__(self, owner, accountType: AccountType):
        self.owner = owner
        self.accountType = accountType
        self.balance = 0

    def withdraw(self, amount):
        if amount > self.balance:
            raise Exception('Can not withdraw more money than balance')
        if amount < 0:
            raise Exception('Can not withdraw a negative amount')
        self.balance -= amount

    def deposit(self, amount):
        if amount < 0:
            raise Exception('Can not deposit a negative amount')
        self.balance += amount

    def __str__(self):
        return 'The owner is ' + self.owner + ', and the account type is ' + self.accountType.name

    def __len__(self):
        return self.balance


class BankUser():

    def __init__(self, owner):
        self.owner = owner
        self.account = {}

    def addAccount(self, accountType):
        if accountType.name in self.account.keys():
            raise Exception(accountType.name + ' account already exists')
        else:
            self.account[accountType.name] = BankAccount(self.owner, accountType)

    def getBalance(self, accountType):
        if accountType.name in self.account.keys():
            return len(self.account[accountType.name])
        else:
            raise Exception(accountType.name + ' account does not exist')

    def deposit(self, accountType, amount):
        if accountType.name in self.account.keys():
            self.account[accountType.name].deposit(amount)
        else:
            raise Exception(accountType.name + ' account does not exist')

    def withdraw(self, accountType, amount):
        if accountType.name in self.account.keys():
            self.account[accountType.name].withdraw(amount)
        else:
            raise Exception(accountType.name + ' account does not exist')

    def __str__(self):
        result = self.owner + ' has ' + str(len(self.account)) + ' accounts. '
        for x in self.account.keys():
            result = result + x + ' account. '
        return result


def ATMSession(bankUser):

    def Interface():
        nonlocal bankUser
        while True:
            print('Enter Option: ')
            print('1) Exit')
            print('2) Create Account')
            print('3) Check Balance')
            print('4) Deposit')
            print('5) Withdraw')

            signal = input()
            if signal not in ['1', '2', '3', '4', '5']:
                print('Invalid operation')
                continue

            if signal == '1':
                print('Successfully exit')
                break
            else:
                print('1) Savings')
                print('2) Checking')

                sub_signal = input()
                if sub_signal not in ['1', '2']:
                    print('Invalid operation')
                    continue

                if signal == '2':
                    if sub_signal == '1':
                        try:
                            bankUser.addAccount(AccountType.SAVINGS)
                            print('Successfully create Savings account')
                            print(str(bankUser))
                        except Exception as e:
                            print(e)
                    else:
                        try:
                            bankUser.addAccount(AccountType.CHECKING)
                            print('Successfully create Checking account')
                            print(str(bankUser))
                        except Exception as e:
                            print(e)

                if signal == '3':
                    if sub_signal == '1':
                        try:
                            balance = bankUser.getBalance(AccountType.SAVINGS)
                            print(f'Savings account balance is {balance}')
                        except Exception as e:
                            print(e)
                    else:
                        try:
                            balance = bankUser.getBalance(AccountType.CHECKING)
                            print(f'Checking account balance is {balance}')
                        except Exception as e:
                            print(e)

                if signal == '4':
                    if sub_signal == '1':
                        try:
                            bankUser.deposit(AccountType.SAVINGS, 0)
                            print('Enter Integer Amount, Cannot be Negative: ')
                            try:
                                amount = int(input())
                            except:
                                print('Invalid amount')
                                continue
                            bankUser.deposit(AccountType.SAVINGS, amount)
                            print('Successfully deposit')
                        except Exception as e:
                            print(e)
                    else:
                        try:
                            bankUser.deposit(AccountType.CHECKING, 0)
                            print('Enter Integer Amount, Cannot be Negative: ')
                            try:
                                amount = int(input())
                            except:
                                print('Invalid amount')
                                continue
                            bankUser.deposit(AccountType.CHECKING, amount)
                            print('Successfully deposit')
                        except Exception as e:
                            print(e)

                if signal == '5':
                    if sub_signal == '1':
                        try:
                            bankUser.withdraw(AccountType.SAVINGS, 0)
                            print('Enter Integer Amount, Cannot be Negative: ')
                            try:
                                amount = int(input())
                            except:
                                print('Invalid amount')
                                continue
                            bankUser.withdraw(AccountType.SAVINGS, amount)
                            print('Successfully withdraw')
                        except Exception as e:
                            print(e)
                    else:
                        try:
                            bankUser.withdraw(AccountType.CHECKING, 0)
                            print('Enter Integer Amount, Cannot be Negative: ')
                            try:
                                amount = int(input())
                            except:
                                print('Invalid amount')
                                continue
                            bankUser.withdraw(AccountType.CHECKING, amount)
                            print('Successfully withdraw')
                        except Exception as e:
                            print(e)

    return Interface


if __name__ == '__main__':
    # test ATM closure
    user = BankUser('Joe')
    interface = ATMSession(user)
    interface()
