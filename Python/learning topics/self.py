

class Employee:
    company = "Google"
    salary = 50000
    def getsalary(self):
        print("Salary is:",self.salary) # self.salary is the same as Employee.salary and prints the salary of the object 


e = Employee()
e.salary = 13333
e.getsalary()