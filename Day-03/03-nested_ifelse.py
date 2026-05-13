# Conditional statements with comparison operators(<=, >=, ==, !=)
# the way of working this conditional statement is if the condition is true the first code block is printed on the console else the else statement is printed on the console.

print("Welcome to the rollercoastr!")
height = int(input("What is your height in cm?"))

if height >= 120:
    print("You can ride the rollecoaster!")
    age = int(input("what is your age?"))
    if age < 12:
        print("The price is 5$")
    elif age <= 12 and age >= 18:
        print("The price is $7")
    elif age > 18:
        print("The price is $12")
else:
    print("Sorry, you have to grow taller before you can riede.")
    print("You can not ride the rollecoaster!")