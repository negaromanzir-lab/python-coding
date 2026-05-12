# Don't chenge the code below 
age = input("What is your current age?")
# Don't chenge the code the above

# Write your code below this line
age = int(age)

end_life = 90
end_week = 90 * 52
end_month = 90 * 12
end_day = 90 * 365

your_day = age * 365
your_week = age * 52 
your_month = age * 12

# calculate your left life time is in the following forms

your_day_left = end_day - your_day
your_week_left = end_week - your_week
your_month_left = end_month - your_month

print(f"You have {your_day_left} days, {your_week_left} weeks, and {your_month_left} months left.")