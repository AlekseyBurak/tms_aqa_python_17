class Employee:

    NUMBER = 0
    def __init__(self, name_employee: str,  salary: int):
        Employee.NUMBER += 1
        self.name_employee = name_employee
        self.salary = salary


    def __str__(self):
        return f"My name is {self.name_employee}. My salary is {self.salary}"

    def __gt__(self, other):
        return self.salary > other.salary

    @property
    def get_name(self):
        return self.name_employee

    @staticmethod
    def new_new():
        print("static")


new = Employee("New", 500)
new1 = Employee("Anna", 900)
print(Employee.NUMBER)

print(new < new1)