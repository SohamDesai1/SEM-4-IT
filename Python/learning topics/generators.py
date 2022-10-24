def gen(n):
    for i in range(n):
        yield i

g= gen(5)
print(g)