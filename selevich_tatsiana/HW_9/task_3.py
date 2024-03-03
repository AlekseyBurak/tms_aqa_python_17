class Room:
    def __init__(self, height: float, width: float, depth: float) -> None:
        """
        :param height: room height
        :param width: room width
        :param depth: room depth
        """
        self.height = height
        self.width = width
        self.depth = depth
        self.floor_area = width * depth
        self.wall_area = (height * depth) * 2 + (height * width) * 2
        self.non_working_wall_area = 0

    def set_non_working_surface_dimensions(self, width: float, height: float) -> None:
        """
        This function sets the dimensions of the non-working surface.
        :param width: non-working surface width
        :param height: non-working surface height
        """
        self.non_working_wall_area += width * height

    def get_work_area_walls(self) -> float:
        """
        This function returns the dimensions of the working surface of the walls.
        :return: working surface of the walls
        """
        return self.wall_area - self.non_working_wall_area


room = Room(2, 3, 4)
room.set_non_working_surface_dimensions(1,1)
room.set_non_working_surface_dimensions(2,2)

print(room.get_work_area_walls())
