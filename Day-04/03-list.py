# list is a data structure that can hold multiple items in a single variable. Lists are ordered, changeable, and allow duplicate values. They are defined by enclosing the items in square brackets [].
# Example of a list
fruits = ["apple", "banana", "cherry"]
# Accessing items in a list
print(fruits[0])  # Output: apple
print(fruits[1])  # Output: banana
print(fruits[2])  # Output: cherry  
# Modifying items in a list
fruits[1] = "blueberry"
print(fruits)  # Output: ['apple', 'blueberry', 'cherry']   
# Adding items to a list
fruits.append("orange") 
print(fruits)  # Output: ['apple', 'blueberry', 'cherry', 'orange']
# Removing items from a list    
fruits.remove("apple")
print(fruits)  # Output: ['blueberry', 'cherry', 'orange']  
# List can contain different data types
my_list = ["Hello", 42, 3.14, True] 
print(my_list)  # Output: ['Hello', 42, 3.14, True]
# List can also contain other lists (nested lists)
nested_list = [1, 2, [3, 4], 5]
print(nested_list)  # Output: [1, 2, [3, 4], 5]

#if the index is negative, it counts from the end of the list. For example, -1 refers to the last item, -2 refers to the second last item, and so on.
print(fruits[-1])  # Output: orange
print(fruits[-2])  # Output: cherry
print(fruits[-3])  # Output: blueberry

# extend() method is used to add multiple items to the end of a list. It takes an iterable (like another list) as an argument and adds each item from that iterable to the list.
fruits.extend(["grape", "melon"])
print(fruits)  # Output: ['blueberry', 'cherry', 'orange', 'grape', 'melon']

# If you want to want see all the methods you can use google "python list methods" and you will find a lot of methods that you can use with lists.