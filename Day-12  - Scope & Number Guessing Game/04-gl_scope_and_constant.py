#constant and global variable
PI = 3.14159 #constant variable, by convention we use uppercase letters to indicate that this variable should not be changed
URL = "https://www.google.com" #constant variable, by convention we use uppercase letters to indicate that this variable should not be changed

def calculate_circumference(radius):
    circumference = 2 * PI * radius
    return circumference

print(calculate_circumference(5))