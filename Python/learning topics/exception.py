f = open("dw.txt", "r")
try:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    print(num1/num2)
except Exception as e:
    print("Please enter only numbers")

else:
    print("No exception")
        
finally:
    print("AYOOOO")   
    f.close() 
     