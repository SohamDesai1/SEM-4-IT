f = open("soham.txt")
# c = f.read(4)
# print(c)
print(f.readline(),end="")
print(f.tell())
print(f.seek(0))
print(f.readline(),end="")
f.close()


with open("soham.txt") as f:
    print(f.readline(),end="")
    print(f.tell())
    print(f.seek(0))
    print(f.readline(),end="")