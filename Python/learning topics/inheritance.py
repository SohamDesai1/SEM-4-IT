
class Employee:
    company = "Google"
    salary = 50000
    def getsalary(self):
        print("Salary is:",self.salary)

class Programmer(Employee):
    language = "Python"

    def getlanguage(self):
        print("Language is:",self.language)

e = Programmer()
e.getsalary()