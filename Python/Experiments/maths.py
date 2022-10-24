import mathmodule

try:
    x1 = float(input("enter the x1 co-ordinate value  : "))
    x2 = float(input("enter the x2 co-ordinate value  : "))
    y1 = float(input("enter the y1 co-ordinate value  : "))
    y2 = float(input("enter the y1 co-ordinate value  : "))

    myResult = mathmodule.MyMathLibrary.calculateEuclideanDistance(x1, x2, y1, y2)
    print(f"The Euclidean Distance Of X1 : {x1}, X2 : {x2}, Y1 : {y1}, Y2 : {y2} Is {myResult} units.")

except:
    print("kindly enter valid co-ordinates value.")