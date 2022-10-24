def print_pyramid(n):
    k = (n - 1)
    for i in range(0, n):
        for j in range(0, k):
            print(end=" ")
        k = k - 1
        for j in range(0, i + 1):
            print("* ", end="")
        print('\r')


if __name__ == "__main__":
    print_pyramid(5)
