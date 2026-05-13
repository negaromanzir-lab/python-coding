# Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j' 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome To the PyPassword Generato!")
nr_letters = int(input("How many letters would you like in your passord?\n"))
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))

# Eazy level 
# fghf^&23
password = ""

for char in range(1, nr_letters + 1):
    password += random.choice(letters)

for char in range(1, nr_symbols + 1):
    password += random.choice(symbols)

for char in range(1, nr_numbers + 1):
    password += random.choice(numbers)

print(password)

# Hard level
# g^2jk8&

password_list = []

for char in range(1, nr_letters + 1):
    password_list += random.choice(letters)

for char in range(1, nr_symbols + 1):
    password_list += random.choice(symbols)

for char in range(1, nr_numbers + 1):
    password_list += random.choice(numbers)

print(password_list)

# so in  this case how we can chenge the order of the items in the list.
# you have to google this one by typing this one :- how to chnage the order of the items in the list python
# by using shuffle() method 

random.shuffle(password_list)
print(password_list)

hard_password = ""

length = len(password_list)

for i in password_list:
    hard_password += i
print(f"Your password is: {hard_password}")