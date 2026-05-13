# Body mass index calculators
# BMI = weight(kg)/height^2 (m^2)

# Dont chenge the code below 
height = input("Enter yuor height in m : ")
weight = input("Enter your weight in kg : ")
# don't chenge the code the above

#write the code below this line

bmi =  round(float(weight) / (float(height) ** 2))

print("Your body mass Index is : " + str(bmi) + " kg/m^2")

if bmi < 18.5:
    print("Underweight")
elif bmi >= 18.5 and bmi < 25:
    print("Normal weight")
elif bmi >= 25 and bmi < 30:
    print("Overweight")
elif bmi >= 30 and bmi < 35:
    print("Obese")
else:
    print("Clinically obese")