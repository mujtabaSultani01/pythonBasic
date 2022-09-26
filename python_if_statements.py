# Here we've simple program which take number as input and tell us the number is odd or even.
number = 9
if number%2 == 0:
    print("your inserted number is even: ", number)
else:
    print("your inserted number is add: ", number)

# We can also take inputs from users...
# By default the taken value in python is string so if we want integer we have to convert it.
num = input("Enter a number: ")
num = int(num)
if num == 0:
    print("You inserted Zero: ", num)
elif num%2 == 0:
    print("Your inserted number is even: ", num)
else:
    print("Your inserted number is add: ", num)

# Now let's have a program which tell you which cuisine you have entered.
afghani = ["Kabuli_Palaw", "Kabab", "Rosh"]
indian = ["Samosa", "Daal", "Naan"]
chinese = ["egg role", "pot sticker", "fried rice"]

choice = input("Type your favorite food to tell you about it's country: ")
if choice in afghani:
    print("You selected afghanis cuisine: ", choice)
elif choice in indian:
    print("You selected indian food: ", choice)
elif choice in chinese:
    print("You selected chinese cuisine: ", choice)
else:
    print("Opps! sorry you didn't selected afghanis, indian or chinese cuisine: ", choice)