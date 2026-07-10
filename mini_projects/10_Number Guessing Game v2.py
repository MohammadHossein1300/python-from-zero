secret_number = 25
attempts = 0



while True:

    guess = int(input("guess the number:"))

    attempts +=1

    if guess < secret_number:
        print("Too low!")

    elif guess > secret_number:
        print("Too high!")


    else:
        print("Correct!")
        print("You guessed it in" , attempts , "attempts")
        break