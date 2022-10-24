class Programmer:
    company = "Google"
    def __init__(self, name, department):
        self.name = name
        self.department = department
        print("The name is", self.name ,"and the department is", self.department)

a = Programmer('John', 'Laptop')
b = Programmer('Mary', 'Desktop')