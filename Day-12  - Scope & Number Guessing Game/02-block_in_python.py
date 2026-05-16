#There is no block scope in python, only function scope. This means that variables defined inside a block (like an if statement or a for loop) are still accessible outside of that block. However, variables defined inside a function are not accessible outside of that function.

game_level = 6 #global scope

def create_enemy():
    enemies = ["Skeleton", "Zombie", "Alien"] 
    if game_level < 5:
        new_enemy = enemies[0]
    print(new_enemy)

create_enemy()