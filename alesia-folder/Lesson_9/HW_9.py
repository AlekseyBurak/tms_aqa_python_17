#############################
# About the Line length

print("\nTask 'Line'\n")
class Line:

    left_border = int(input("Left border: "))
    right_border = int(input("Right border: "))
    length: int

    def find_length(self):
        if self.left_border >= 0:
            Line.length = Line.right_border - Line.left_border
        elif self.right_border >= 0:
            Line.length = abs(Line.left_border) + Line.right_border
        else:
            Line.length = abs(Line.left_border) - abs(Line.right_border)


line1 = Line()
line1.find_length()
print(f"Length of line is: ", line1.length)


###############################
# About the Bank card
print("\nTask 'Bank card'\n")
class BankCard:
    card_num = str(input("Input a card number: "))
    name_holder = str(input("Input a holder name: "))
    __cvv = int(input("Input a cvv number: "))

    def card_number(self):
        print("A bank card number is:", self.card_num[0:4], self.card_num[4:8],
              self.card_num[8:12], self.card_num[12:16], sep=" ")

    def card_holder(self):
        print("A card holder name is:", self.name_holder)

card1 = BankCard()
card1.card_number()
card1.card_holder()

##################################
# About the Room
print("\nTask 'Room working square'\n ")
class Room:

    def __init__(self, height: float, width: float, length: float):
        self.height = height
        self.width = width
        self.length = length
        self.walls_s: float
        self.floor_s: float
        self.door_s: float
        self.window_s: float

    def doors(self, h_door, w_door):
        self.door_s = h_door * w_door

    def windows(self, h_window, w_window):
        self.window_s = h_window * w_window

    def room_square(self):
        self.walls_s = (2 * self.height * (self.width + self.length)
                        - self.door_s - self.window_s)

my_room = Room(3.1, 4.2, 5)
print(f"Room dimensions: {my_room.height}m * {my_room.width}m * {my_room.length}m")
my_room.doors(2.5, 1.2)
print(f"Door size: {my_room.door_s}m2")
my_room.windows(1.5, 1)
print(f"Window size: {my_room.window_s}m2")
my_room.room_square()
print(f"Working square of the room is: {my_room.walls_s}m2")