# CS207, HW2, Problem 3(a)

def make_withdraw(balance):
    def withdraw(amount):
        if (amount < 0) or (amount > balance):
            print('Invalid Withdraw')
            return None
        else:
            return balance-amount
    return withdraw


wd = make_withdraw(5000)
print(wd(500))
print(wd(1000))

print('This function does not behave correctly, since we do not update balance after withdrawal. The balance remains '
      'unchanged no matter how we withdraw.')

