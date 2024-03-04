class Room:
    def __init__(self):
        self.hight_room = int(input("Введите высоту комнаты:"))
        self.width_room = int(input("Введите ширину комнаты:"))
        self.depth_room = int(input("Введите глубину комнаты:"))
        self.S_pola = self.width_room * self.depth_room
        self.S_Stena = 2 * (self.hight_room * self.width_room + self.hight_room * self.depth_room)

    def get_window_square(self, window_hight, window_width):
        window_square = window_hight * window_width
        self.S_Stena -= window_square
    def get_door_square(self, door_hight, door_width):
        door_square = door_hight * door_width
        self.S_Stena -= door_square
    def get_all_Stena_square(self):
        return self.S_Stena
    def get_all_room_square(self):
        room_square = self.S_pola + self.S_Stena
        return room_square


room = Room()
room.get_window_square(5,2)
room.get_door_square(2,3)
print(room.get_all_Stena_square())
print(room.get_all_room_square())