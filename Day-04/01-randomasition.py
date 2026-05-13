# In this code prictes the randomisation of numbers using the random module in python
# module is a built-in library in python that provides functions for generating random numbers and performing random operations. The randint() function is used to generate a random integer between the specified range (inclusive). In this case, it generates a random integer between 1 and 10 and prints it to the console.

import random
import mymodule
# Generate a random integer between 1 and 10
random_integer = random.randint(1, 10)
print(random_integer)
# Accessing the value of pi from the mymodule
print(mymodule.pi)

random_float = random.random()
print(random_float)

# how to create a random decimal between 0 and 5
random_decimal = random.random() *5
print(random_decimal)

#for to generate a random love score between 1 and 100
love_score = random.randint(1, 100)
print(love_score)