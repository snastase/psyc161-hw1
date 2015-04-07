"""Module for estimation of factorial (Homework #1)

Takes a non-negative integer n, and returns n!
"""

from nose.tools import assert_equal, assert_greater_equal


def factorial_recursive(n):
    import warnings
    try:
        n = int(n)
    except ValueError:
        print "Unable to convert input n to integer!"
    if n == 1 or n == 0:
        factorial = 1
        return factorial
    elif n < 0:
        n = abs(n)
        warnings.warn("""
            Input n must be non-negative, converting to absolute value""")
        factorial = n * factorial_recursive(n - 1)
        return factorial
    else:
        factorial = n * factorial_recursive(n - 1)
        return factorial


def factorial_nonrecursive(n):
    try:
        n = int(n)
    except ValueError:
        print "Unable to convert input n to integer!"
    factorial = 1
    for i in range(1, n+1):
        factorial = factorial * i
    return factorial


def factorial_numpy(n):
    from numpy import prod
    try:
        n = int(n)
    except ValueError:
        print "Unable to convert input n to integer!"
    factorial = int(prod(range(1, n+1)))
    return factorial


def factorial_scipy(n):
    import scipy.misc
    try:
        n = int(n)
    except ValueError:
        print "Unable to convert input n to integer!"
    factorial = int(scipy.misc.factorial(n))
    return factorial


def test_factorial():
    for method in (factorial_recursive, factorial_nonrecursive,
                   factorial_scipy):
        assert_equal(method(0), 1)
        assert_equal(method(1), 1)
        for i in range(2, 11):
            assert_equal(method(i) % 2, 0)
            assert_greater_equal(method(i), i)
    for i in range(0, 11):
        assert_equal(factorial_recursive(i), factorial_nonrecursive(i),
                     factorial_scipy(i))


def speed_test():
    from timeit import Timer
    t = Timer("factorial_recursive(10)",
              "from factorial import factorial_recursive")
    print "Recursive:", t.timeit(10000)
    t = Timer("factorial_nonrecursive(10)",
              "from factorial import factorial_nonrecursive")
    print "Non-recursive:", t.timeit(10000)
    t = Timer("factorial_numpy(10)",
              "from factorial import factorial_numpy")
    print "Numpy non-recursive:", t.timeit(10000)
    t = Timer("factorial_scipy(10)",
              "from factorial import factorial_scipy")
    print "Scipy factorial:", t.timeit(10000)

if __name__ == '__main__':
    # This is a way to determine either file was "executed", so if it was
    # imported (by e.g. nose) as a library, we should not run code
    # below

    nconditions = raw_input("Please enter number of conditions: ")
    norders = factorial_recursive(nconditions)
    print("Number of possible trial orders: " + str(norders))
