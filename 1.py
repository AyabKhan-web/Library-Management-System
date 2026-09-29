class Employee:
    companyName = "Apple"
    NoOfEmployees = 0

    def __init__(self, name):
        self.name = name
        self.raise_amount = 1.0
        Employee.NoOfEmployees += 1
    def display(self):
        print(f"Employee name is {self.name} in {self.companyName} of size {self.NoOfEmployees} employees and the amount is raised {self.raise_amount}")

emp1 = Employee("Lucy")
# emp1.name = "Ahmad"
emp1.companyName = "Honda"
emp1.raise_amount = 1.3
emp1.display()

emp2 = Employee("Mark")
emp2.raise_amount = 1.1
emp2.companyName = "Apple Pakistan"
emp2.display()