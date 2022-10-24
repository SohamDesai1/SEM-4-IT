class Programmer:
    company = "Google"
    def __init__(self, name, department,salary):
        self.name = name
        self.department = department
        self.salary = salary
        
    def printDetails(self):
        print("The name is", self.name ,"and the department is", self.department, "and the salary is", self.salary)
        
    # OPERATOR OVERLOADING 
    def __add__(self, other):
        return self.salary + other.salary
    
    def __repr__(self):
        return f"Programmer('{self.name}','{self.department}',{self.salary})"
    
    def __str__(self):
        return "The name is", self.name ,"and the department is", self.department, "and the salary is", self.salary
        
emp = Programmer("John", "IT",12000)
emp1 = Programmer("Jane", "IT",15000)
print(str(emp))