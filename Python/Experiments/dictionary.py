Keys = int(input("Enter the number of keys you want to add in dictionary : "))
myDict = {}
for i in range(Keys):
    keys = input("Enter the Keys In The Dictionary : ")
    value = input("Enter the Values In The Dictionary : ")
    myDict[keys] = value
while True:
    print("1.Update dictionary")
    print("2.Delete any key from dictionary")
    print("3.Find any value of keys from dictionary")
    print("4.Display dictionary")
    print("0.Exit")
    choice = int(input("Enter your choice :"))
    if choice==1:
        uKey = input("Enter key to update :")
        if uKey in myDict:
            uValue = input("Enter the updated value : ")
            myDict[uKey]=uValue
            print(myDict)
        else:
            print("Enter a valid input")
    elif choice==2:
        dKey = input("Enter key to delete :")
        if dKey in myDict:
            del myDict[dKey]
            print(myDict)
        else:
            print("Enter a valid input")
    elif choice==3:
        fKey = input("Enter key to find :")
        if fKey in myDict:
            print(myDict[fKey])
        else:
            print("Enter a valid input")
    elif choice==4:
        print(myDict)
    elif choice==0:
        exit()        
                        