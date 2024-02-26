import random

print("Bulls & Cows")

robot_num = list()
for i in range(0, 4):
    robot_num.append(random.randint(0, 9))
    i += 1
print(robot_num)
robot_num_str = [str(j) for j in robot_num]

mess = "Input a 4-digit number: "

while True:
    player_num = list(input(mess))
    def count(pl_n: list):
        # print(pl_n)
        bulls = 0
        cows = 0
        for x in pl_n:
            if x in robot_num_str:
                if pl_n.index(x) == robot_num_str.index(x):
                    bulls += 1
                else:
                    cows += 1
        if bulls == 4:
            print("You've guessed the number and won!")
            return
        else:
            print("Bulls =", bulls, "\nCows =", cows)

    print(count(player_num))




