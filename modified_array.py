# 1. *Create a function* that takes an array, an index, and a value as parameters.
#Inside the function, use the insert method to insert the value at the specified index in the array. Return the modified array.

def insert_as_index(arr, index, value):
    arr.insert(index, value)
    return arr

my_arr = [1, 2, 3, 6, 7, 8, 9, 10]
modified_arr = insert_as_index(my_arr, 4, 5)
print(modified_arr)