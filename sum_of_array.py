# *Create a function* that takes an array of numbers as a parameter.
#  Use a while loop to calculate and return the sum of all the numbers in the array.

def sum_array(numbers):
    total = 0
    index = 0
    while index < len(numbers):
        total += numbers[index]
        index += 1
    
    return total

numbers = [1, 2, 3, 4, 5]

print(sum_array(numbers))