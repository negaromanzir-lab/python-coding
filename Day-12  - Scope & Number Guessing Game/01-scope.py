#scope in programming refers to the region of a program where a variable is defined and can be accessed. There are two main types of scope: global scope and local scope.
enemies = 1 #global spcope
def increase_enemies():
    enemies = 2 #local scope
    print(f"enemies inside function: {enemies}")

increase_enemies()
print(f"enemies outside function: {enemies}")