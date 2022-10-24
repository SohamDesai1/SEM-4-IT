# MAP FUNCTIONS
num = ["2","3","4","5","6","7","8","9","10"]
num = list(map(int,num))
print(num)

num1 = [2,3,2,5,6,7,8,9,10]
square = list(map(lambda x: x**2,num1))
print(square)

fu = [lambda x: x**2,lambda x: x**3]
for i in range(5):
    val = list(map(lambda x: x(i),fu))
    print(val)