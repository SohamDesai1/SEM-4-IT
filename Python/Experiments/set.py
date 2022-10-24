from secrets import choice


a = input("Enter first string:")
b = input("Enter second string:")

f = set(a)
f1 = set(b)

for i in range(len(f)):
    f.add(a[i])

for i in range(len(f1)):
    f1.add(b[i])

while True:
    print("1.Display common elements")
    print("2.Display elements in a but not in b")
    print("3.Display union of a and b")
    print("4.Display elements present in both a and b but not common")
    print("0.Exit")
    
    choice = int(input("Enter your choice: "))
    
    if choice == 1:
        print("Common elements: ", f.intersection(f1))
    elif choice == 2:
        print("Elements in a but not in b: ", f.difference(f1))
    elif choice == 3:
        print("Union of a and b: ", f.union(f1))
    elif choice == 4:
        print("Elements present in both a and b but not common: ", f.symmetric_difference(f1))
    elif choice == 0:
        exit()    
    else:
        print("Invalid choice")
    
        