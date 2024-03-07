class Worker:
    def __init__(self, name: str, salary: int):
        self.name = name
        self.salary = salary

    def __str__(self):
        return f"My name {self.name}. My salary {self.salary}"

    def __gt__(self, other):
        return self.salary > other.salary