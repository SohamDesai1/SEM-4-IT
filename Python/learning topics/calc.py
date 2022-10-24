class Calculator:
    def __init__(self, num1):
        self.num1 = num1

    def sqr(self):
        return self.num1 ** 2

    def cube(self):
        return self.num1 ** 3

    def sqrroot(self):
        return self.num1 ** 0.5

    def display(self):
        print(self.num1)


a = Calculator(2)
print(a.sqr())
print(a.cube())
print(a.sqrroot())
