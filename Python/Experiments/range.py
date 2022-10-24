r = int(input("Enter The Range (1-n) To Get The Number's Divisible By 4 : "))
if (r < 4):
    print("No Numbers Found, Enter Range Greater Than 3 To Get Some Output Number's.")

else:
    for i in range(1, r):
         if (i % 4 == 0):
             print(i , end=" ")
