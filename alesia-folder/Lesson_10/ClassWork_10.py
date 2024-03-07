class PropertyClass:

    def __init__(self):
        self.ordinary = 1
        self._private = 2
        self.__protected = "I'm protected argument"

    @property
    def protected(self):
        return self.__protected

    @protected.setter
    def protected(self, value):
        self.__protected = value

    # def get_protected(self):
    #     return self.__protected
    #
    # def set_protected(self, value):
    #     self.__protected = value
    @protected.deleter
    def protected(self):
        del self.__protected

pr = PropertyClass()

# print(pr._PropertyClass__protected)
# pr._PropertyClass__protected = 5
# print(pr._PropertyClass__protected)


print(pr.protected)
pr.protected = 5
print(pr.protected)
# del pr.protected
# print(pr.protected)

pr1 = PropertyClass()

print(pr.ordinary)
print(pr1.ordinary)

pr.ordinary = 5
pr1.ordinary = 56.89

print(pr.ordinary)
print(pr1.ordinary)

#########
class MyClass:

    TOTAL_OBJECT = 0

    def __init__(self):
        MyClass.TOTAL_OBJECT += 1
        self.some_instance_data = 4

    @staticmethod
    def foo():
        return 1

    @classmethod
    def total_objects(cls):
        print("Total objects:", cls.TOTAL_OBJECT)
        cls.foo()

my_obj1 = MyClass()

MyClass.total_objects()

class Cat:
    def __init__(self):
        self.paws = 4
        self.tail = True
        self.__lives = 9

    @property
    def lives(self):
        return self.__lives

murzik = Cat()

murzik.paws = 5
murzik.tail = 0

# murzik.__lives += 1
# print(murzik.__lives)
murzik.__lives = 10
print(murzik.__lives)
print(murzik._Cat__lives)
print(murzik.lives)

class Worker:

    NUMBER_OF_WORKERS = 0
    def __init__(self, name: str, salary: int):
        Worker.NUMBER_OF_WORKERS += 1
        self.name = name
        self.salary = salary

    def __str__(self):
        return f"My name is {self.name}. My salary is {self.salary()}"
    def __gt__(self, other):
        return self.salary > other.salary
    @property
    def r_name(self):
        return self.name
    @staticmethod
    def static():
        return "static"


mike = Worker("Mike", 10_000)
jim = Worker("Jim", 20_000)
print(Worker.NUMBER_OF_WORKERS)
print(mike < jim)
print(mike.r_name)
print(Worker.static())