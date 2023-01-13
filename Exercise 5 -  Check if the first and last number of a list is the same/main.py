#Exercise from https://pynative.com/python-basic-exercise-for-beginners/
# Check if the first and last number of a list is the same
#Write a function to return True if the first and last number of a given list is same. If numbers are different then return False.

def check_same (n):
  print("Given list: ", n)

  firstNum = n[0]
  lastNum = n[-1]
  
  if firstNum == lastNum:
    return True
  else:
    return False

n_x = [10, 20, 30, 40, 10]
print("The result is", check_same(n_x))

n_y = [75, 65, 35, 75, 30]
print ("The result is", check_same(n_y))


    
