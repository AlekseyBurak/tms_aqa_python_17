# def decor(type1):
#     def wrapper(func):
#         def inner(*args):
#             converted = []
#             # converted = [type1(i) for i in args]
#
#             for i in args:
#                 if type(i) is type1:
#                     converted.append(i)
#                 else:
#                     converted.append(type1(i))
#                 return func(*args)
#             # print(f"Adding of params {args} is {func(*args)}")
#
#         return inner
#     return wrapper
#
# @decor(type1=int)
# def add_symbols(*args):
#     s1 = sum(args)
#     return s1
# @decor(type1=str)
# def add_symbols2(*args):
#     s2 = "".join(args)
#     return s2
#
# print(add_symbols(2, 4, 5, 6))
# # print(add_symbols(2, 4, 5, 6, '7'))
#
# print(add_symbols2("a", "b", "c"))
# # print(add_symbols2("a", "b", "c", 7))
import time


#########################################################
class Pet:

    def __init__(self, name: str, weight: float, color: str):
        self.weight = weight
        self.name = name
        self.color = color
        self.paws = 4
        self.tail = True

    def sleep(self):
        print("i sleep")

    def call(self):
        print("i'm here")

class MyCat(Pet):

    def __init__(self, name: str, weight: float, color: str):                        #surname: str, farther_name : str = None,
        super().__init__(name, weight, color)                                     #, angry: bool = False):     #konstruktor klassa

    paws = 4
    _claws = 18

    # name = "Luna"

    def sleep(self):
        print(f"My name is {self.name}. I'm about to sleep in 5 sec")
        time.sleep(5)
        print("I've slept already")

    def eat(self):
        print("Yum yum")

    def go(self):
        print("I move fast")

    def cut_claws(self, num: int):
        self._claws -= num

    def give_claws(self):
        return self._claws

class MyDog:

    def __init__(self, name: str,                         #surname: str, farther_name : str = None,
                 weight: float, angry: bool = False):     #konstruktor klassa
        self.name = name
        self.weight = weight
        self.angry = angry

    paws = 4
    __claws = 16
    tail = True
    # name = "Luna"

    def sleep(self):
        print(f"My name is {self.name}. You want me to sleep...")
        time.sleep(3)
        print("No, we go for a walk")

    def eat(self):
        print("Yum yum")

    def go(self):
        print("I move fast")

    def bark(self):
        print("WOOF")


luna = MyCat(name="Luna", weight=4.5, color="white")
print(luna.name)

elza = MyDog(name="Elza", weight=5.3)
print(elza.name)

print(luna._claws)
print(elza._MyDog__claws)

luna.cut_claws(5)
print(luna.give_claws())

luna.sleep()
elza.sleep()