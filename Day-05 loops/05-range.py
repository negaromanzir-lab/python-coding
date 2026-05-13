# Range function to loop through an items
# this i sprint the numbers between 1 and 11 but not included the number 11 and steps by three

for number in range(1, 11, 3):
    print(number)

# To find the total number in the range 
# to find the total numbers between 1 and 101 not included 101 in this range
total = 0
for number in range(1, 101):
    total += number
print(total)