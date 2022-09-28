# Function is a block of code that performs a specific task.
# Function make your code more modular and more readable.
# Let's have an example to add two persons list without function.
Tom_exp_list = [3000, 5000, 4300, 5400]
Joe_exp_list = [4300,9300, 3400, 5600]
total = 0
for item in Tom_exp_list:
    total = total + item
print("Toms' total expense are: ", total)
total = 0
for item in Joe_exp_list:
    total = item + total
print("Joe tatal expenses are: ", total)

""" 
so now look we're writing the similar code twice.
if we have 100 lists then we should write it 100 times which is not good practice.
so to avoid this we can use Function. in Python def keyword can be used to define function.
"""
def calculate_total(exp):
    total = 0
    for item in exp:
        total = item + total
    return total

toms_total = calculate_total(Tom_exp_list)
joes_total = calculate_total(Joe_exp_list)

print("Toms total expense are: ", toms_total)
print("Joes total expenses are: ", joes_total)

# Let's see other example of adding two numbers:

def sum(a, b):
    total = 0
    total = a + b
    return total

num1 = 20
num2 = 30
result = sum(num1, num2)
print("Sum of given numbers is: ", result)

# We can get input from user:
num3 = input("Type num1: ")
num4 = input("Type num2: ")

num3 = int(num3)
num4 = int(num4)
result1 = sum(num3, num4)
print("The result for given numbers is: ", result1)
