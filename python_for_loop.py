# For working with for loop, let's have a simple problem:
# Store monthly expenses in a list and find out the total expenses for all months.
exp = [3200, 5400, 3400, 2800, 6300]
total_exp = exp[0] + exp[1] + exp[2] + exp[3] + exp[4]
print("Your total expenses for five months are: ", total_exp)

# So now you see that without loop if want to add all expenses we're force to point to every element separately which
# is not a best way, if we have 1000 element then we should point to each of them.
# So to overcome this problem we can use loop simply:

total = 0
for item in exp:
    total = item + total
print("total expenses in last five moths are: ", total)

# We can use range function with for loop to print numbers in a specific range.
for i in range(1, 20):
    print(i)
    # print(i*i)

# If we want to print the month number with its expense we can do it:
total_expenses = 0
for i in range(len(exp)):
    print("Month: ", (i+1), "Expense: ", exp[i])
    total_expenses = exp[i] + total_expenses
    print("Total expense are: ", total_expenses)

# Let's have another example of finding the key of your car...
key_location = "chair"
locations = ["garage", "living_room", "chair", "closet"]
for i in locations:
    if i == key_location:
        print("Key is found at: ", i)
        break
    else:
        print("Key is not found in: ", i)
        
