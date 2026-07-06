password = (input("Enter your password:"))

if len(password) < 8:
    print("Password is too short.")

else:
    print("Password accepted.")