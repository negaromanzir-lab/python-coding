# FizzBuzz Game challenges
#        How it works 
# if the number devide by 3 print "Fizz"
# if the number devide by 5 print "Buzz"
# if the number devide by both 3 and 5 print "FizzBuzz"
# other ways print thr number

for number in range(1, 101):
    if number % 3 == 0 and number % 5 != 0:
        print("Fizz")
    elif number % 5 == 0 and number % 3 != 0:
        print("Buzz")
    elif number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    else:
        print(number)



# Or you can solve on this way
for number in range(1, 101):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)