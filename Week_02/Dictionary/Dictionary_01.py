# Data Types: Dictionary

# key : value relationship
#dicti = {"Burak Talha": "Python", "Ali": "C++","Veli": "Java"}
dicti_2 = {1 : [1,2,3,4,5], 2 : [6,7,8,9,10]}

# Keys method will return all keys
"""
print(type(dicti_2.keys()))

print(dicti_2.values())
a = dicti_2.values()


print(dicti_2.items()) """
array = []
i = 1
for i in range(0,len(dicti_2)):
    array = array + [dicti_2.get(i)]
    i+=1

print(array)



