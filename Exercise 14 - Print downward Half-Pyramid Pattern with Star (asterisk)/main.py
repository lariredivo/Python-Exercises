#Exercise from https://pynative.com/python-basic-exercise-for-beginners/
#Exercise 14: Print downward Half-Pyramid Pattern with Star (asterisk)

for n in range(6, 0, -1):
  for m in range(0, n - 1):
    print("*", end=" ")
  print(" ")
