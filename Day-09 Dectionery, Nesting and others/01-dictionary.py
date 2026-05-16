# it's worked kind of dictionary like in real worlds.
# in the form of key value pair like tables.
# is in {key: value}
dic = {"fname": "Negaro", "lname":"Manzir"}
programming_dictionary = {
    "Bug":"An error in a program from running as expected.", 
    "Function": "A piece of code that you can easily call over and over again.",
    "loop": "The action of doing something over again and again."
}

# retrieving tha data from the dictionary
# print(programming_dictionary["Bug"])

#adding a new data to the dictionary
programming_dictionary["new"] = "This is the new item"

# creating an empty dictionary.
empty_dictionary = {} #and add like empty_dictionary[]

#Wipe or clear an existing dictionary
#programming_dictionary = {}
#print(programming_dictionary)

# Edit an item in a dictionary
programming_dictionary["Bug"] = "The bug discription is edited"
print(programming_dictionary)

#looping through a dictionary
for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])