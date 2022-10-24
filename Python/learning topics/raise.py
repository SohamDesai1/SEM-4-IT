a = input("Enter first number: ")
b = input("Enter second number: ")
if a.isalpha() :
    raise Exception("Please enter only numbers")
if int(b) == 0:
    raise ZeroDivisionError("Please enter a number other than 0")

 