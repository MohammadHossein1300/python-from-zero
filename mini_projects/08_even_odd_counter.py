number = int (input("Enter number:"))
even_numbers = 0
odd_numbers = 0


for i in range(1,number  + 1):
    
    if i % 2 == 0:
        even_numbers += 1
    elif i % 2 != 0:
        odd_numbers += 1


print("even_numbers:" , even_numbers)
print("odd_numbers:" , odd_numbers)
















