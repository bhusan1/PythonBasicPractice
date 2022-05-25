friend_ages = {"Rolf": 24, "Adam": 30, "Anne": 27}

print(friend_ages["Adam"])
#Output: 30


# add element and value
friend_ages["Bob"]= 20
print(friend_ages)
# Output: {'Rolf': 24, 'Adam': 30, 'Anne': 27, 'Bob': 20}

#update element and value
friend_ages["Rolf"]= 20
print(friend_ages)
#Output: {'Rolf': 20, 'Adam': 30, 'Anne': 27, 'Bob': 20}

# printing name and age

for friend , age in friend_ages.items():
    print(f"{friend}: {age}")
# Output:
#Rolf: 20
#Adam: 30
#Anne: 27
#Bob: 20

#finding average age
age_values = friend_ages.values()
print(sum(age_values)/len(age_values))
#Output: 24.25