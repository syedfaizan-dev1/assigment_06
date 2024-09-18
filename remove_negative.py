#*Write a program* that has an array of numbers; if the number is negative,
#it should remove the negative number from the array.

array = [1, -2, 3, -4, 5, -6, 7, -8, 9, 10]

count = 0

while count < len(array):
    remove_negative = array[count]
    if remove_negative < 0:
        array.pop(count)
    count += 1
print(array)    

