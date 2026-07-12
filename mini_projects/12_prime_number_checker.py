while True:

   is_prime = True

   num = int(input("Enter number:"))


   if num < 2:
    print("Not Prime Number")
    continue

   for i in range(2 , num):
      if num % i == 0:
         is_prime = False
         break


   if is_prime == False:
      print("Not Prime Number")
   else:
       print("Prime Number")
      
    