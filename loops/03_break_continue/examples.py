for i in range(1, 11):
    if i == 6:
        break

    print(i)



    for i in range(1, 11):
     if i == 6:
        continue

    print(i)



    while True:
     text = input("Type 'exit' to quit: ")

    if text == "exit":
        break

    print("You entered:", text)