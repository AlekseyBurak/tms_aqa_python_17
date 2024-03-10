class Cat:
    def __init__(self, name: str, surname: str, fathers_name: str = None):
        self.name = name
        self.FIO = f"Name - {name}, Surname - {surname}, Fathers name - {fathers_name}" \
        if fathers_name else f"Name {name} surname {surname}"

    paws = 4
    tail = True
    claws = 18

    def cut_claws(self, num: int):
        self.claws -= num

lada = Cat(name="alex", surname="Chumakou", fathers_name="Chumakou")
print(lada.FIO)

