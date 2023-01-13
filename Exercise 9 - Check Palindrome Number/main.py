#Exercise from https://pynative.com/python-basic-exercise-for-beginners/
# Check Palindrome Number
# Write a program to check if the given number is a palindrome number.
#A palindrome number is a number that is same after reverse. For example 545, is the palindrome numbers
number = input("Write a number to check if is a palindrome number: ")
print("Original number ", number)

#convert number to string
num_string = str(number)

#reverse the string
reverse_num = "".join(reversed(num_string))


if number == reverse_num:
  print("Yes. given number is palindrome number")
else:
  print("No. given number is not palindrome number")
