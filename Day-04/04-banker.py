import random

# Split string method 
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
print(names)
select_name = random.randint(0, len(names) - 1)
print(f"{names[select_name]} is going to buy the meal today!")


# by using method choise
person_who_will_pay = random.choice(names)
print(f"{person_who_will_pay} is going to buy the meal today!")