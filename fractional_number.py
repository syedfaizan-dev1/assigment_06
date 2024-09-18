# *Create a function* that takes a positive integer as a parameter and
#uses a while loop to calculate and return the factorial of that number.

def fractional(n):
    if n < 0:
        raise ValueError("Input must be positive integer.")
    result = 1
    while n > 1:
        result *= n
        n -= 1
    return result


print(fractional(5))