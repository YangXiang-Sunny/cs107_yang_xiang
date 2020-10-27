# CS207, HW4, Problem4: A Toy AD Implementation

class AutoDiffToy():

    def __init__(self, val):
        self.val = val
        self.der = 1

    def __add__(self, other):
        try:
            # Duck typing two AutoDiffToy objects
            res = AutoDiffToy(self.val + other.val)
            res.der = self.der + other.der
            return res
        except AttributeError:
            # Handle float / int case
            if (type(other) == float) or (type(other) == int):
                res = AutoDiffToy(self.val + other)
                res.der = self.der
                return res
            else:
                raise Exception('Error! Type not acceptable!')

    def __radd__(self, other):
        return AutoDiffToy.__add__(self, other)

    def __mul__(self, other):
        try:
            # Duck typing two AutoDiffToy objects
            res = AutoDiffToy(self.val * other.val)
            res.der = self.der * other.val + self.val * other.der
            return res
        except AttributeError:
            # Handle float / int case
            if (type(other) == float) or (type(other) == int):
                res = AutoDiffToy(self.val * other)
                res.der = self.der * other
                return res
            else:
                raise Exception('Error! Type not acceptable!')

    def __rmul__(self, other):
        return AutoDiffToy.__mul__(self, other)


if __name__ == '__main__':
    a = 2.0  # Value to evaluate at
    x = AutoDiffToy(a)

    alpha = 2.0
    beta = 3.0

    # Case 1
    f = alpha * x + beta
    print(f.val, f.der)

    # Case 2
    f = x * alpha + beta
    print(f.val, f.der)

    # Case 3
    f = beta + alpha * x
    print(f.val, f.der)

    # Case 4
    f = beta + x * alpha
    print(f.val, f.der)


