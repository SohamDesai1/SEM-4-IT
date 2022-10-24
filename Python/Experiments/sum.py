
def sum_digits(n):
    if n < 10:
        return n
    else:
        return n % 10 + sum_digits(n // 10)

n = int(input("Enter a number: "))
print(sum_digits(n))
