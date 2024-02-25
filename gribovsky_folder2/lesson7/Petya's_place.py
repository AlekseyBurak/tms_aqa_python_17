# rank = [165, 163, 162, 160, 157, 157, 155, 154]
# x = 154

def position(rank: list, x: int):
    petya_place = 1
    for ind in range(len(rank)):
        if rank[ind] >= x:
            petya_place += 1
    print(f"Петя займет {petya_place} место в строю")


position([165, 163, 162, 160, 157, 157, 155, 154], 162)