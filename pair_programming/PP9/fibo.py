# Start writing code here...
# Discussed whether to calculate the sequence in Fibonacci
# or in FibonacciIterator
# Also discussed whether to store the whole sequence 
# or just update the two previous values.

class Fibonacci:
    def __init__(self,n):
        self.n = n
        
    def __iter__(self):
        return FibonacciIterator(self.n) 


class FibonacciIterator:
    def __init__(self, n):
        self.n = n
        self.index = 0
        self.previous2 = 0
        self.previous1 = 1
    
    def __next__(self):
        #print('ind=',self.index)
        #print(self.n)
        if self.index < self.n:
            current = self.previous1 + self.previous2
            self.previous2 = self.previous1
            self.previous1 = current
            self.index += 1
            return current
        else:
            raise StopIteration()
    
    def __iter__(self):
        return self
        
fib = Fibonacci(10)
print(list(iter(fib)))


