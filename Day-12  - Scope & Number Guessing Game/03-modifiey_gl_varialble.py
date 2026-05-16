#modifying the global variable

enemies = 1

def increase_enemies():
    global enemies #this tells python that we want to use the global variable 'enemies' instead of creating a new local variable with the same name
    enemies += 1
    print(f"enemies inside function: {enemies}")
    
increase_enemies()
print(f"enemies outside function: {enemies}")