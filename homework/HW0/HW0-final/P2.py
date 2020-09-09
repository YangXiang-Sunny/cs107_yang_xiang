# Problem 2

# Part 2.1
from math import sqrt
def numbers(name:str, n:int):
    assert name=="pi" or name=="golden"
    assert type(n) == int
    
    if name == 'pi':
        res = 0
        for i in range(1,n):
            res += float(1)/(i**2)
        res = sqrt(6*res)
        return res
    
    if name == 'golden':
        fib = [1,1]
        assert n>1
        for i in range(1,n-1):
            fib.append(fib[i]+fib[i-1])
        return (fib[n-1]/fib[n-2])

print(numbers("golden",10))
print(numbers("pi",10))

# Part 2.2
pi_num = list(range(2,200,10))
golden_num = list(range(2,20))
pi_list = [numbers("pi",x) for x in pi_num]
golden_list = [numbers("golden",x) for x in golden_num]

# Part 2.3
import matplotlib.pyplot as plt
import numpy as np
plt.plot(pi_num,pi_list)
plt.title(r"$\pi$")
plt.axhline(np.pi,color = "red")
plt.show()

plt.plot(golden_num,golden_list)
plt.title(r"$\phi$")
phi = (sqrt(5)+1)/2
plt.axhline(phi,color = "red")
plt.show()
