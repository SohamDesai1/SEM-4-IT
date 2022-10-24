# check prime number
n = int(input("Enter a number: "))
flag = False
for i in range(2, n):
    if n % i == 0:
        flag = True
        break

if flag == True:
    print("not Prime")
else:
    print("Prime")
    