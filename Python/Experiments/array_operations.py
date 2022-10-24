a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

sum = sum(i for i in a if i % 2 == 0)
print("The sum of even elements is", sum)

print("The no of elements divisible by 3 are", len([x for x in a if x % 3 == 0]))
a.append(11)
a.append(12)
print(a)

a = [x for x in a if x % 2 == 0]
print(a)
