# List in Python
# Lists syntax 

#[]
notes = ["Mehmet",80,70,50,100]

persons = ["burak","talha","nisa nur","rana gül","dağcan",5,6.2,True]
i = 0

print(notes)

# Writes the notes list
for i in range(0,notes.__len__()):
    print(notes[i])
    i = i + 1
    
# In list querying variable tips

print(type(notes[0])) #int)

# Returns 5. variable in notes list
#print(type(notes[5])) #str

# For 'deposit all list' query

all_list = notes + persons

print(all_list)

