num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
a = num1
num1 = num2
num2 = a
print("After swapping: ")
print("First number: ", num1)
print("Second number: ", num2)

if num1 < 0:
    print("First number is negative")
elif num1 > 0:
    print("First number is positive")
else:
    print("First number is zero")

if num2 < 0:
    print("Second number is negative")
elif num2 > 0:
    print("Second number is positive")
else:
    print("Second number is zero")

