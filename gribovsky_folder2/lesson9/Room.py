class Room:
    def __init__(self, height: float, depth: float, width: float):
        self.height = height
        self.depth = depth
        self.width = width
        self.floor_sq = depth * width
        self.walls_sq = 2 * depth * height + 2 * width * height

    def windows(self, wind_width: float, wind_height: float, wind_number: int) -> float:
        print(f"There are {wind_number} windows in the room")
        windows_sq = wind_number * wind_width * wind_height
        print(f" windows area = {windows_sq}")
        return windows_sq

    def doors(self, door_width: float, door_height: float, door_number: int) -> float:
        print(f"There are {door_number} doors in the room")
        doors_sq = round(door_number * door_height * door_width, 3)
        print(f" doors area = {doors_sq}")
        return doors_sq

    def useful_wall_sq(self, doors, windows) -> float:
        useful_wall_sq = round(self.walls_sq - (windows + doors), 3)
        print(f"useful room's area = {useful_wall_sq}")
        return useful_wall_sq


living_room = Room(2.5, 3.2, 4.1)
print(living_room.floor_sq)
print(living_room.walls_sq)
living_room.windows(1.5, 1, 2)
living_room.doors(0.75, 1.9, 2)
living_room.useful_wall_sq(doors=2.85, windows=3)
