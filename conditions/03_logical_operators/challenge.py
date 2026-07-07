age = int(input("Enter your age:"))
id = (input("Has id?(yes/no)"))


if age >= 18 and id == "yes":
   
    print("Access granted.")

elif age < 18:
    print("Too young.")

elif age >= 18 and id != "yes":
    print("ID required.")

else:
   print ("Access denied.")