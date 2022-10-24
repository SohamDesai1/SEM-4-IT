# fibonacci series
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


num = int(input("Enter till where you want to print fibonacci series: "))
for i in range(0, num):
    print(fibonacci(i), end=" ")
