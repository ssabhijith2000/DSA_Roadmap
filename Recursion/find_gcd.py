# How to find the greatest common divisor of two numbers using recursion?
#Euclidean algorithm -- gcd(48,18) is #
# step1 : 48/18 =2 remainder 12
# step 2 : 18/12 = 1 remainder 6
# step 3 : 12/6 =2 remiander 0
# constraints : only positive numbers, convert negsative numbers to positive numbers
def gcd(a, b):
    assert int(a) == a and int(b) == b, 'The numbers must be integre onlyl!'
    if a < 0:
        a = -1 * a
    if b < 0:
        b = -1 * b
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


print(gcd(48, 18))
