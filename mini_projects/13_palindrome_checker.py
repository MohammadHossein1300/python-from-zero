
while True:

    text = (input("Enter:"))

    reverse_text = (text[::-1])

    if text==reverse_text:
        print("Palindrome")
    else:
        print("Not Palindrome")