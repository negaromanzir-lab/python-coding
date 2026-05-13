# pizza Deliveries Programs 
print("Welcome to Python pizza Deliveries")
size = input("What size pizza do yuo want? S, M, or L ")
add_peppperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")

bill = 0

if size == "S":
    bill += 15
    if add_peppperoni == "Y":
        bill += 2
        if extra_cheese == "Y":
            bill += 1
elif size == "M":
    bill += 20
    if add_peppperoni == "Y":
        bill += 3
        if extra_cheese == "Y":
            bill += 1
elif size == "L":
    bill += 25
    if add_peppperoni == "Y":
        bill += 3
        if extra_cheese == "Y":
            bill += 1
print(f"Your final bill is: ${bill}")