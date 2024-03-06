# class MyClass1:
#
#     def foo(self):
#         print('foo')
#
# class MyClass2:
#
#     def bar(self):
#         print('bar')
#
# class Cat(MyClass1, MyClass2):
#
#     # def __init__(self):
#     #     super().__init__()
#
#     def baz(self):
#         self.foo()
#
# cat = Cat()
#
# cat.baz()

# class Worker:
#
#     def __init__(self, name: str, salary: int):
#         self.name = name
#         self.salary = salary
#
#     def __str__(self):
#         return f"My name is {self.name}. My salary is{self.salary}"
#
#     def __gt__(self, other):
#         return self.salary > other.salary
#
# Al = Worker("Al", 10_000)
# La = Worker("La", 10_000)

# print(Al > La)

class Worker:
    NUMBER_OF_WORKERS = 0

    def __init__(self, name: str, salary: int):
        Worker.NUMBER_OF_WORKERS += 1
        self.name = name
        self.salary = salary

    @property
    def worker_name(self):
        return self.name

    @staticmethod
    def work_without_worker():
        print('Work_without_worker')

    def __str__(self):
        return f"My name is {self.name}. My salary is{self.salary}"

    def __gt__(self, other):
        return self.salary > other.salary


Al = Worker("Al", 10_000)
La = Worker("La", 10_000)

print(Al > La)

my_worker = Worker
print(Worker.work_without_worker())
