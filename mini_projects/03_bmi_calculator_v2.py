first_name = input("Enter your name:")

height = float(input("Enter your height:"))

weight = float(input("Enter your weight:"))

bmi = round (weight / (height**2),2)


print("=======================")

print("BMI CALCULATOR")

print("=======================")

print("Name:",first_name)
print("BMI:",bmi)

if bmi < 18.5:
    print("Underweight")

elif bmi >= 18.5 and bmi < 25:
    print("Normal")

elif bmi >= 25 and bmi < 29.9:
    print("Owerweight")

else:
    print("Obese")

print("=======================")
