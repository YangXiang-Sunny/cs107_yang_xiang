# CS207, HW2, Problem 3(c)

def make_withdraw(balance):
    def withdraw(amount):
        nonlocal balance
        if (amount < 0) or (amount > balance):
            print('Invalid Withdraw')
            return None
        else:
            balance -= amount
            return balance
    return withdraw


wd = make_withdraw(5000)
print(wd(500))
print(wd(1000))
