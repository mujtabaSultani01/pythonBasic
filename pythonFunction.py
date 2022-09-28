# Function is a block of code that performs a specific task.
# Function make your code more modular and more readable.
# Let's have an example to add two persons list without function.
Tom_exp_list = [3000, 5000, 4300, 5400]
Joe_exp_list = [4300,9300, 3400, 5600]
total = 0
for item in Tom_exp_list:
    total = total + item
print("Toms' total expense are: ", total)

for item in Joe_exp_list:
    total = item + total
print("Joe tatal exxpenses are: ", total)

# so now look we're writing the similar code twice.
# if we have 100 lists then we should write it 100 times which is not good practice.
# so to avoid this we can use Function.
# in Python def keyword can be used to define function.


