first_number = int(input("Enter first number:"))

second_number = int(input("Enter second number:"))

operation =(input("Choose opertion (+,-,/,*):"))


if operation == "+":

    print(first_number + second_number)

elif operation == "-":

    print(first_number - second_number)

elif operation == "/":

    print(first_number / second_number)

elif operation == "*":

    print(first_number * second_number)    

else:
    print("Invalid operation!")   

