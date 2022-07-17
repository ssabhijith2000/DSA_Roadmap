def factorial(n):
    assert n >= 0 and int(
        n) == n, 'The number must be a positive integer only!'
    if n < 1:
        return 1
    else:
        return n * factorial(n-1)


print(factorial(- 1))
