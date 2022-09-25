# Python list work based on array concept. using String we were storing each item in separate variable & thus each character was storing in separate index.
item1 = "bread"
item2 = "Pasta"
item3 = "Fruits"
items = item1 + ", " + item2 + " and " + item3;
print("your stored items are: ", item1, ", ", item2, " and ", item3)
print("your stored items are: ", items)

# Sometimes we need to store multiple items in single variable so for that we can use lists which has special structure.
itemsList = ["bread", "Pasta", "Fruits"]
print("your stored items using list are: ", itemsList)

# in lists each item is stored in separate index not each character.
print(itemsList[0])
print(itemsList[1])
print(itemsList[2])

# We can also overwrite each list item.
itemsList[0] = "Apple"
print("zero index item 'bread' is overwrite, new item is: ", itemsList[0])

# if we want to print part of the list, same as String we can print it:
print(itemsList[0:1])
print(itemsList[:2])
print(itemsList[1:])
print(itemsList[-1])

# We can append item to a list
itemsList.append("Banana")
print(itemsList)

# We can insert an item into specific position using insert function
itemsList.insert(1,"Peach")
print(itemsList[1])
print(itemsList)

# We can simply join two lists
kitchenTool = ["knife", "plate", "Glass"]
print(kitchenTool)
totalItems = itemsList + kitchenTool
print(totalItems)

# To find length of list, simply we can use len() function.
print("the length of fruits list is: ", len(itemsList), " the length of kitchen list is: ", len(kitchenTool))

# To find a specific item in a list, we can use (in) operators
print("Apple" in itemsList)
print("Apple" in kitchenTool)

# That's were all about Python lists....




