# How to find the sum of digits of a positive integer number using recursion

def sumOfDigits(n):
    if n == 0:
        return 0
    else:
        return int(n % 10) + sumOfDigits(int(n//10))


print(sumOfDigits(112))
