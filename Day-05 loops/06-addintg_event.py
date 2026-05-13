# In tis code challenges you have to calculate the sum of the even numbers from 1 to 100, include 1 and 100

total = 0

for number in range(1, 101):
    if number % 2 == 0:
        total += number
print(f"The total number of even number between 1 to 100 is : {total}")

# or You can use this one 
total1 = 0
for number in range(2, 101, 2):
    total1 += number
print(f"The second way of solve this problems {total1}")