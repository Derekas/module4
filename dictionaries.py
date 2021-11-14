dictionary = {"cat": "chat", "dog": "chien", "horse": "cheval"}
phone_numbers = {'boss': 5551234567, 'Suzy': 22657854310}
empty_dictionary = {}

print(dictionary)
print(phone_numbers)
print(empty_dictionary)
'''insert'''
dictionary["cat"]="larry"
dictionary["bird"]="baries"
dictionary.update({"beetle":"Peter"})
'''del'''
del dictionary["cat"]
dictionary.pop("dog")
for elem in dictionary.keys():
    print(dictionary[elem])