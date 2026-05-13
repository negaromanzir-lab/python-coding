# used for checking the multiple conditioanal statements and the others
# Like= and, or, not

# Conditional statements with comparison operators(<=, >=, ==, !=)
# the way of working this conditional statement is if the condition is true the first code block is printed on the console else the else statement is printed on the console.

print("Welcome to the rollercoastr!")
height = int(input("What is your height in cm?"))

bill = 0

if height >= 120:
    print("You can ride the rollecoaster!")
    age = int(input("what is your age?"))
    if age < 12:
        bill = 5
        print("Child ticket are 5$.")
    elif age <= 18:
        bill = 7
        print("Youth tickets are $7.")
    elif age >= 45 and age <= 55:
        print("Everything is going to be ok, Have a free ride on us!")
    else:
        bill = 12
        print("Adult tickets are $12.")
    wants_photo = input("Do you want a photo take? Y or N.")
    if wants_photo == "Y":
        bill += 3
    print(f"Your final bill is ${bill}")   

else:
    print("Sorry, you have to grow taller before you can riede.")
    print("You can not ride the rollecoaster!")