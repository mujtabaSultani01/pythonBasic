# Files in python. // creating and writing in files:
F = open("C:\\users/Habib/PycharmProjects/pythonBasic/funny.txt", "w")
F.write("I love Python.")
F.write("\nI love JavaScript.")
F.write("\nI love PHP.")
F.close()

# Reading file. // we want to read file 'funny1.txt' and count each line words...
# one short display:
F_read = open("C:\\users/Habib/PycharmProjects/pythonBasic/funny1.txt", "r")
print(F_read.read())
F_read.close()

# split() method will split the stirng using input character and return a list (array) of words.
F_read1 = open("C:\\users/Habib/PycharmProjects/pythonBasic/funny1.txt", "r")
for line in F_read1:
    tokens = line.split(' ')
    #print(str(tokens))
    print(len(tokens))
F_read1.close()