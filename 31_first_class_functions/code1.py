def search (sequence, expected, finder):
    for elem in sequence:
        if finder(elem) == expected:
            return elem
    raise RuntimeError(f"Could not find an element with {expected}.")

friends = [
    {"name": "Bob Smith", "age": 25 },
    {"name": "Ben Patel", "age": 23 },
    {"name": "Jen Hana", "age": 20 },
]

def get_friend_name(friend):
    return friend["name"]

print(search(friends, "Bob Smith", get_friend_name))