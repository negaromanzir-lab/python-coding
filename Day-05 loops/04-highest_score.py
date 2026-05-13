# Highest score exercises
student_score =input("Input the list of student score").split()
for n in range(0, len(student_score)):
    student_score[n] = int(student_score[n])
print(student_score)
# In this code challenges not use the max method so you have to use the for loop for this challenges. goes head.....

# write your logic here below
highest_score = 0
for h in student_score:
    if h > highest_score:
        highest_score = h

print(f"The highest score in the class is : {highest_score}")