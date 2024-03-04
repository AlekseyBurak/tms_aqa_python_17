
class Room:
    def __init__(self, door_area, window_area):
        self.door_area = door_area
        self.window_area = window_area
        self.height_room = float(input("Enter height_room:"))
        self.width_room = float(input("Enter width_room:"))
        self.length_room = float(input("Enter depth_room:"))
        self.wall_area = 4 * ((self.height_room * self.width_room) + (self.height_room * self.length_room))


    def calculation_wall_area(self):
        work_wall_area = self.wall_area - (self.door_area + self.window_area)
        return work_wall_area

room = Room(1, 6)
print(room.wall_area)
work_wall_area = room.calculation_wall_area()
print(f"The working surface of the walls excluding doors and windows: {work_wall_area}")








    #print(f"Floor_area: {floor_area:.2f})



