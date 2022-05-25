#list, tupple and sets to deine many var at once
l = ['Bob', 'Ram', 'Shyam'] #list
t = ('Bob', 'Ram', 'Shyam') # tupple
s = {'Bob', 'Ram', 'Shyam'} # set

# you cant modify a tupple | list can be added and removed items
# set cannot have duplicate elements but you can add remove items
# list and tupple keep the order of elements
# set does not keep order

# printing
print(l[0])
print(t[1])

# modifying list (tupple cannot be modified)
l[0] = "Ben"
print (l)
#Output
# ['Ben', 'Ram', 'Shyam']

# adding in list
l.append("Bob") #append adds at end
print (l)
#Output
# ['Ben', 'Ram', 'Shyam', 'Bob']

l.remove("Bob")

# adding in set
s.add("Sita")
print(s)
# {'Ram', 'Bob', 'Sita', 'Shyam'}