#performing math in 1 list and adding onto another
numbers = [1, 3, 5]
doubled = []

for num in numbers:
    doubled.append(num*2)

print(doubled)

#we can do this in short way by:
# doubled = [num*2 for num in numbers]

# ***********************************************************************
# another example for comprehension
friends = ["Ram", "Shyam", "Hari", "Raghu"]
starts_r = [friend for friend in friends if friend.startswith("R")] # this is comprehended code for code in comment below

print(starts_r)

# this code can be also written as above
#friends = ["Ram", "Shyam", "Hari", "Raghu"]
#starts_r = []

#for friend in friends:
#    if friend.startswith("R"):
#        starts_r.append(friend)

        