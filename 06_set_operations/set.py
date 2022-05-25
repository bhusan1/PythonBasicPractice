friends = {"Ram", "Shyam", "Sita", "Geeta"}
abroad = {"Ram", "Geeta"}

# difference in elements of 2 sets
local_friends = friends.difference(abroad)
print(local_friends)
# {'Sita', 'Shyam'}

# empty set
other_friends = abroad.difference(friends)
print(other_friends)
# set() ---empty set output

# adding sets
not_friends = {"Hari", "Gopal"}
people = friends.union(not_friends)
print(people)
# {'Gopal', 'Sita', 'Hari', 'Geeta', 'Ram', 'Shyam'}

# intersection
ex_girlfriend = {"Sita", "Rita"}
bothFriandGf = ex_girlfriend.intersection(friends)
print (bothFriandGf)
# {'Sita'}