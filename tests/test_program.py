"""File to test the usage of pyheat scipt."""


def powfun(a, b):
    """Method to raise a to power b using pow() function."""
    return pow(a, b)


def powop(a, b):
    """Method to raise a to power b using ** operator."""
    return a**b


def powmodexp(a, b):
    """Method to raise a to power b using modular exponentiation."""
    base = a
    res = 1
    while b > 0:
        if b & 1:
            res *= base
        base *= base
        b >>= 1
    return res


def main():
    """Test function."""
    a, b = 2377757, 773
    pow_function = powfun(a, b)
    pow_operator = powop(a, b)
    pow_modular_exponentiation = powmodexp(a, b)


if __name__ == '__main__':
    main()
