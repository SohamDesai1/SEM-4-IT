# menu driven calculator
while True:
    print("Select operation.")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5.Modulus")
    print("0. Exit")
    choice = int(input("Enter choice: "))
    if choice == 0:
        break
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    if choice == 1:
        print(num1, "+", num2, "=", num1 + num2)
    elif choice == 2:
        print(num1, "-", num2, "=", num1 - num2)
    elif choice == 3:
        print(num1, "*", num2, "=", num1 * num2)
    elif choice == 4:
        print(num1, "/", num2, "=", num1 / num2)
    elif choice == 5:
        print(num1, "%", num2, "=", num1 % num2)
    else:
        print("Invalid input")
print("Thank you for using calculator.")
