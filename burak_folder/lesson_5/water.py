litter_3 = 0
litter_5 = 0
print(f"{litter_3=}, {litter_5=}")

while litter_5 != 4:
    command = input(
        """
    Press 1 if you want to fill 3-liter bucket
    Press 2 if you want to fill 5-liter bucket
    Press 3 if you want to empty 3-liter bucket
    Press 4 if you want to empty 5-liter bucket
    Press 5 if you want to pour from 3-liter bucket to 5-liter bucket
    Press 6 if you want to pour from 5-liter bucket to 3-liter bucket
    Press 7 if you want to stop this game
    """
    )
    if command == "1":
        litter_3 = 3
    elif command == "2":
        litter_5 = 5
    elif command == "3":
        litter_3 = 0
    elif command == "4":
        litter_5 = 0
    elif command == "5":
        if litter_5 <= 2:
            litter_5 += litter_3
            litter_3 = 0
        if litter_5 > 2:
            space = 5 - litter_5
            if space >= litter_3:
                litter_5 += litter_3
                litter_3 = 0
            elif space < litter_3:
                litter_3 -= space
                litter_5 += space
    elif command == "6":
        if litter_3 > 0:
            space = 3 - litter_3
            if space >= litter_5:
                litter_3 += litter_5
                litter_5 = 0
            elif space < litter_5:
                litter_5 -= space
                litter_3 += space
        elif litter_3 == 0:
            litter_3 = litter_5
            if litter_3 > 3:
                litter_3 = 3
            litter_5 -= 3
            if litter_5 < 0:
                litter_5 = 0
    elif command == "7":
        break
    print(f"{litter_3=}, {litter_5=}")
