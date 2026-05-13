# This is Difficult Challenge
#Don't chenge the code below
year = int(input("Enter the year you want to check ")) 
#Don't chenge the code above

if year % 4 == 0:
    if year % 100 != 0:
        if year % 400 == 0:
            print("Leap")
        else:
            print("Not Leap")
    else:
        print("Leap")
else:
    print("Not Leap")