# CS207, HW4, Problem4: A Toy AD Implementation

class AutoDiffToy():

    def __init__(self, x, alpha=1, beta=0):
        self.x = x
        self.alpha = alpha
        self.beta = beta
        self.val, self.der = self.forward()

    def forward(self):
        # Calculate values of function and derivative with forward AD
        x1 = self.x
        d1 = 1.0
        v1 = self.alpha * x1
        d2 = self.alpha * d1
        v2 = v1 + self.beta
        d3 = d2
        f, f_diff = v2, d3
        return f, f_diff

    def __add__(self, other):
        try:
            x, alpha, beta = other.x, other.alpha, other.beta
            if self.x == other.x:
                return AutoDiffToy(self.x, self.alpha + other.alpha, self.beta + other.beta)
            else:
                raise Exception("Error! Two AutoDiffToys have different x values!")
        except AttributeError:
            if (type(other) == float) or (type(other) == int):
                return AutoDiffToy(self.x, self.alpha, self.beta+other)
            else:
                raise Exception('Error! Type not acceptable!')

    def __radd__(self, other):
        return AutoDiffToy.__add__(self, other)

    def __mul__(self, other):
        try:
            x, alpha, beta = other.x, other.alpha, other.beta
            raise Exception("Error! Can not multiply two AutoDiffToys!")
        except AttributeError:
            if (type(other) == float) or (type(other) == int):
                return AutoDiffToy(self.x, other * self.alpha, other * self.beta)
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


