# Avirage Height Exercise
student_heights = input("Input the list of student heights ").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
print(student_heights)

#Not use this one you have to use for loop to solve this problems
# number_of_student = len(student_heights)
# average_height = round(total_height / number_of_students)
# print(average_height)

# Write your code here
total_height = 0
number_of_students = 0

for student in student_heights:
    total_height += student
    number_of_students += 1

average_height = total_height / number_of_students
int(round(average_height))
print(f"The avirage of the student is: {average_height}")