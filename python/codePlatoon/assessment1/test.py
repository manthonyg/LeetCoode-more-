class Employee:
    num_employee = []
    def __init__(self,name):
        self.name = name
        self.num_employee.append(self.name)
    
employee1 = Employee('hi')
employee2 = Employee('hello')

print(employee1.name)
print(employee1.num_employee)
print(Employee.num_employee)
