#*Write a program* to remove all the odd numbers from an array.

array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_number = []
index = 0

while index < len(array):
    if array[index] % 2 == 0:
        even_number.append(array[index])
    index += 1


print("Even Numbers", even_number)

#2nd method
# for odd in array:
#     if odd % 2 == 0:
#         print(odd)