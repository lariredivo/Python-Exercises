#Exercise from https://pynative.com/python-basic-exercise-for-beginners/
#Create a new list from a two list using the following condition
#Given a two list of numbers, write a program to create a new list such that the new list should contain odd numbers from the first list and even numbers from the second list.

list1 = [10, 20, 25, 30, 45]
list2 = [40, 45, 60, 75, 90]
list3 = []

for n in list1:
  if n % 2 == 0:
  return n
      for j in list2:
        if j % 3 == 0:
        return j

        list3 = n + j
        print(list3)

