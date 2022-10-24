list = [1,2,3,4,5,6,7,8,9,10]
def isGreaterThan5(num):
    return num > 5

isGreaterThan5 = list(filter(isGreaterThan5,list))
print(isGreaterThan5)