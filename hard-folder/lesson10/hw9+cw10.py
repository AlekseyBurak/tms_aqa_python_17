#задача на площадь
class Room:
    def __init__(self):
        self.shirina = int(input())
        self.vysota = int(input())
        self.glubina = int(input())
        self.pl_pol = self.shirina * self.glubina
        self.pl_sten = self.vysota * self.glubina

    def door(self, shirina_dv, vysota_dv):
        self.square_dv = shirina_dv * vysota_dv
        self.pl_sten = self.vysota * self.glubina - self.square_dv

    def square(self):
        return self.pl_sten


room = Room()
room.door(1, 5)
print(room.square())

#classwork
class Worker:

    num_workers = 0

    def __init__(self, name: str, zp: int):
        Worker.num_workers += 1
        self.name = name
        self.zp = zp
    @property
    def worker_name(self):
        return self.name

    @staticmethod
    def static():
        print('static')

    def __str__(self):
        return f'My name is {self.name}. My zp is {self.zp}'

    def __gt__(self, other):
        return self.zp > other.zp


worker2 = Worker('worker2', 10000)
worker3 = Worker('worker3', 20000)

print(worker3 > worker2)
print(worker2.__str__())