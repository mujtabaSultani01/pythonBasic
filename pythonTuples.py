# Tuples is list of values grouped together.
point = (5,4)
print(point[0])
# the main difference between list and tuples is: in list all values have similar meaning (Homogenous)
# but in tuples all the values having different meaning (Heterogeneous)
expense_list = [3200, 4300, 5300, 4300]
names_list = ["Ali", "Ahmad", "Fawad", "Faizan"]

print(expense_list)
print(names_list)

address_tuples = ("Bagh Bala", "3rd street", "2nd District", "Kabul-Afghanistan")
points_tuples = (6,5)

print(address_tuples)
print(points_tuples)

# the 2nd difference is, you can change the specific value of specific index in a list but not in tuples.
names_list[0] = "Fayez"
print(names_list)
