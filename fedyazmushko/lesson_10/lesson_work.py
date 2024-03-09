class Rabotnik:

    NUMBER_OF_WORKERS = 0

    def __init__(self, name: str, salary: int):
        Rabotnik.NUMBER_OF_WORKERS += 1
        self.salary = salary
        self.name = name

    def __str__(self):
        return (f"This is salary: {self.salary}"
                f"This is name: {self.name}")


    def __gt__(self, other):
        return self.salary > other.salary

    @property
    def worker_name(self):
        return self.name

    @staticmethod
    def static():
        print("static")


mik = Rabotnik("Mik", 10_000)
jim = Rabotnik("Jim", 10_000)
