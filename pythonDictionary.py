# Dictionaries is something thta allows you to store key-value parties
# also known as Map, Hash tables or associative arrays.
# a classical example will be a phone dicrectory. we can access each value separately using the key.
phone_dir = {
                "Ali": "078444343",
                "Ahmad": "07747733",
                "Mansoor": "07087348"
}
print("Ali phone number is: ", phone_dir["Ali"])
for key in phone_dir:
    print("Name:", key, "\n","Phone:",  phone_dir[key])

# to check if some one is present in dic or not:
print("Ali" in phone_dir)

# To delete all records from dic you can use clear() method:
phone_dir.clear()

