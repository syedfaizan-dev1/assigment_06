# *Implement a program* that takes a list of temperatures in Celsius as input from the user.
# Convert each temperature to Fahrenheit using the formula F = (C * 9/5) + 32 and store the converted temperatures in an array.
# Use a while loop to perform the conversion for each temperature.

def celsius_to_fahrenheit(celsius_temps):
    fahrenheit_temp = []
    index = 0

    while index < len(celsius_temps):
        fahrenheit = (celsius_temps[index] * 9/5) + 32
        fahrenheit_temp.append(fahrenheit)
        index += 1

    return fahrenheit_temp



user_input = input("Enter the temperature sparated by comma: ")
celsius_list = [float(temp.strip()) for temp in user_input.split(',')]

fahrenheit_list = celsius_to_fahrenheit(celsius_list)

print("Temperature in farhenheit:", fahrenheit_list)