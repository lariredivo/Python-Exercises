#Exercise from https://pynative.com/python-basic-exercise-for-beginners/
# Print characters from a string that are present at an even index number
#Write a program to accept a string from the user and display characters that are present at an even index number.

#For example, str = "pynative" so you should display ‘p’, ‘n’, ‘t’, ‘v’.

word = input("Enter word: ")
print("Original String is: ", word)

size = len(word)

print("Printing only even index chars")
for i in range(0, size - 1, 2):
  print(word[i])
