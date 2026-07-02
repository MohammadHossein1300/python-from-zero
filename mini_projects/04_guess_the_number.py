secret_number = 7

guess = int(input("Guess the number:")) 

while guess != secret_number:

    print("Wrong! Try again.")
    guess = int(input("Guess the number:"))

if guess == secret_number:

    print("Congratulations! You guessed correctly.")

    