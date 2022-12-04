# Catch the list variable

persons = ["burak","sipan","kaan","baran","mustafa"]
notes = [[60,70,80,90,100], [50,70,80,90,100]]

print(persons[0:5:3])

print(notes[1][0])


# CRUD operations to the lists

names = ["ali","veli","uçar","koşar","adem","mehmet","adem"]



# CREATE transaction

#names.insert(1,"yusuf")
# Or
names.append("yusuf")


# READ transaction
print(names[::])


# UPDATE transaction
names[1] = "Faruk"

# DELETE transaction
names.pop(2)
#Or
names.remove("adem")

# After change
print(names[:])

# Getting index of the value
print(persons.index("burak"))

# Sorting transaction
persons = persons.sort()



# Slicing for Numbers
numbers = [1,2,3,4,5,6,7,8,9,10]
print(numbers[::2])
