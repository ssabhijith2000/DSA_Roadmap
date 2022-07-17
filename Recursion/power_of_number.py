# How to calculate power of a number using recursion
def power(base, exp):
    assert exp > 0 and int(
        exp) == exp, 'The exponent must be positive integer only'
    if exp < 1:
        return 1
    else:
        return base * power(base, exp-1)


print(power(2, -1))
