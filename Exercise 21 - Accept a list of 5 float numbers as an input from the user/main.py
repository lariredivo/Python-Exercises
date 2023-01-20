#Exercise from https://pynative.com/python-input-and-output-exercise/
#Exercise 21 - Accept a list of 5 float numbers as an input from the user
#Expected output:
#[78.6, 78.6, 85.3, 1.2, 3.5]

input_numbers = input('Enter numbers separated by space ')
user_list = input_numbers.split()
print('list: ', user_list)
