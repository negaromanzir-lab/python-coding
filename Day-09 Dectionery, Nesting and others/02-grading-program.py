student_scores = {
    "Nago": 81,
    "Bona": 99,
    "Abdi": 74,
    "Zaki": 62
}

#TODO-1: Create the empty dictionart called student_grades.
student_grades = {}

#TODO-2: Write your code below to add grades to student_grades.

for name in student_scores:
    if(student_scores[name] > 90):
        student_grades[name] = "Outstanding"
    elif(student_scores[name] > 80):
        student_grades[name] = "Exceeds Expectations"
    elif(student_scores[name] > 70):
        student_grades[name] = "Acceptable"
    else:
        student_grades[name] = "Fail"

print(student_grades)