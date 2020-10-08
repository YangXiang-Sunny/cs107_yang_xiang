# CS207, HW2, Problem 3(b)

def make_withdraw(balance):
    def withdraw(amount):
        if (amount < 0) or (amount > balance):
            print('Invalid Withdraw')
            return None
        else:
            balance = balance - amount
            return balance
    return withdraw


print("This won't work, since if we try to update balance within the inner function, balance will be local "
      "and resolved within the inner function (nearest scope), so it has nothing to do with outer function any more. "
      "And here we use balance in 'if' before updating it, causing an UnboundLocalError "
      "(reference it before assigment).")
wd = make_withdraw(5000)
print(wd(500))
print(wd(1000))