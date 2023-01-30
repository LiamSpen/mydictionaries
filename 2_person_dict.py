person = {}
person["fname"] = "Joe"
person["lname"] = "Fonebone"
person["age"] = 51
person["spouse"] = "Edna"
person["children"] = ["Ralph", "Betty", "Joey"]
person["pets"] = {"dog": "Fido", "cat": "Sox"}

print(person)

# The code below is used to get the 1 item from a list in a dictionary
print(person["children"][1])

# The code below is used to search a dictionary within a dictionart for the value form a key
print(person['pets']['cat'])

# Print all of the names of the children in the dictionary
for child in person["children"]:
    print(child)

# Print out the key and value pairs in the dictionary
for pet, name in person['pets'].items():
    print(f"Type of pet: {pet}, Name of the pet: {name}")
