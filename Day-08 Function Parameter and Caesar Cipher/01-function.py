# function is a block of code which only runs when it is called. You can pass data, known as parameters, into a function. A function can return data as a result.
# creating a function
# creat a  function called greet().
# write 3 print statements inside the function.
# call the greet() function and run the code.
def greet():
    print("This is the function!")
    print("Are ready to learn a  function?")
    print("If Yes, Go head!")

greet()

#Function that allows for input

def greet_with_name(name):
    print(f"Hello {name}")
    print(f"How do you do {name}?")

greet_with_name("Negero")
#parameter is name and argument is "Negero" in the above code. Parameter is a variable that is used in the function definition, while an argument is the actual value that is passed to the function when it is called.