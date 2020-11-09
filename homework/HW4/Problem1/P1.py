# CS107, HW4, Problem1
import numpy as np
import matplotlib.pyplot as plt


def numerical_diff(f, h):

    def eval_diff(x):
        return 1.0 * (f(x+h) - f(x)) / h

    return eval_diff


if __name__ == '__main__':

    # x to be evaluate
    x = np.arange(0.2, 0.4, 0.001)

    # Analytical derivative
    y_analytical_diff = 1.0 / x

    # Finite difference
    hs = [1e-1, 1e-7, 1e-15]
    y_numerical_diff = []
    for h in hs:
        f_diff = numerical_diff(np.log, h)
        y_numerical_diff.append(f_diff(x))

    # Answers to Part C
    # Q-a
    print('Answer to Q-a: h = 1*10^(-7) most closely approximates the true derivative. For too small h, it '
          'amplifies floating point errors, as the line for h=10^(-15) looks zig-zag. For too large h, '
          'the approximation is not accurate, as the line for h=10^(-1) is far from analytical derivative.')
    # Q-b
    print('Answer to Q-b: Automatic differentiation is stable and can evaluate derivatives to machine precision. '
          'Besides, it is less computational costly than symbolic differentiation.')

    # Plot
    plt.figure(figsize=(8, 8))
    plt.plot(x, y_analytical_diff, color='yellow', label='Analytical Derivative')
    plt.plot(x, y_numerical_diff[0], label='Finite Difference with h=$10^{-1}$')
    plt.plot(x, y_numerical_diff[1], alpha=0.5, color='grey', linestyle='--', label='Finite Difference with h=$10^{-7}$')
    plt.plot(x, y_numerical_diff[2], label='Finite Difference with h=$10^{-15}$')
    plt.xlabel('x')
    plt.ylabel("f'(x)")
    plt.title('Comparing Analytical Derivative and Finite Difference')
    plt.legend()
    plt.show()
    # plt.savefig('./P1_fig.png')

