first_name = input("Enter your name:")

height = float(input("Enter your height:"))

weight = float(input("Enter your weight:"))

bmi = round (weight / (height**2),2)

print("=======================")

print("BMI RESULT")

print("=======================")

print("Name:",first_name)
print("BMI:",bmi)

print("=======================")
