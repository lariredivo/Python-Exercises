#Exercise from https://pynative.com/python-basic-exercise-for-beginners/
# Display numbers divisible by 5 from a list
#Iterate the given list of numbers and print only those numbers which are divisible by 5.

n_list = [10, 20, 33, 46, 55]

print("Given list is ", n_list)
print("Divisible by 5:")
for n in n_list:
    if n % 5 == 0:
      print(n)
