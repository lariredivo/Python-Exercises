#Exercise from https://www.youtube.com/watch?v=ODjFDZC_TyA
#Write a program to display the even numbers between 1 to 10

count = 0
for number in range(1, 10):
  if number % 2 == 0:
    count += 1
    print(number)

print(f"The list have {count} even numbers")
