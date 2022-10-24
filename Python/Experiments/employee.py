class Employee:
    co = 0
    def __init__(self, name, salary,id):
        self.name = name
        self.salary = salary
        self.id = id
        Employee.co += 1
    
    def Display(self):
        print("Name :", self.name)
        print("Salary : ",self.salary)
        print("ID : ",self.id)
    def displayCount(self):
        print("Total Employee : ",Employee.co)    
      
emp1 = Employee("Soham Desai",50000,1)
emp2 = Employee("Dhruv Agrawal",30000,2)
emp3 = Employee("Falguni Joshi",40000,3)

emp3.displayCount()
emp1.Display()
emp2.Display()
emp3.Display()


      
            
        