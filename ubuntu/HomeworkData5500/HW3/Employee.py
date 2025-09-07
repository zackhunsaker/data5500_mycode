class Employee:
    def __init__ (self,name,salary):
        self.name = name
        self.salary = salary
    def salaryincrease(self,percent):
        increase_amount = self.salary * (percent/100)
        self.salary += increase_amount
        return self.salary


emp = Employee("John",40000)
updated_salary = emp.salaryincrease(10)

print("The updated Salary is:",updated_salary)

