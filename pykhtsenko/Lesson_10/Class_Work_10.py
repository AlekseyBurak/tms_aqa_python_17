class Worker:

    number_of_workers = 0
    def __init__(self, name: str, pay: int):
        Worker.number_of_workers += 1
        self.name = name
        self.pay = pay

    def __str__(self):
        return f"This is name {self.name}. Pay: {self.pay}"

    def __gt__(self, other):
        return self.pay >  other.pay

    @property
    def worker_name(self):
        return self.name
    @staticmethod
    def job_worker():
        print("I ll be back")


mike = Worker("Mike", 10000)
Jim = Worker("Jim", 500)
print(mike < Jim)