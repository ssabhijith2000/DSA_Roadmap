# How to convert from decimal to binary using recusion
# Steps
# Step1: Divide the number by 2
# Step 2 : Get the integer qoutient for the next iteration
# Step 3 : Get the remainder for the binary digit
# Step 4 : Pepeat the steps until the quotient is equal to 0
# to get the output multiply previous sum of remainder with 10 and add the present remainder
# and repeat it in every iteration

def decimal_to_binary(n):

    if n/2 == 0:
        return 0
    else:
        return n % 2 + 10 * decimal_to_binary(int(n/2))


print(decimal_to_binary(10))
