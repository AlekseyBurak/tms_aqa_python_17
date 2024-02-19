# GAME OF BUCKETS
print("-"*55 + "WELCOME" + "-"*55)
print("""Welcome to the Bucket Game, where we dive into the exciting world of bottle challenges!
Today's challenge comes from Die Hard 3. We have two unique buckets: one holds 3 litres and the other holds 5 litres.
Our goal is to fill one of the buckets with exactly 4 litres of liquid.""")

print("-"*52 + "START OR END" + "-"*52, "\nEnter START if you want to start the game\nEnter END if you want to get out")
start = input("START OR END?:\n")
while start != "START" and start != "END":
    print("Afraid to lose? Try again")
    start = input("START OR END?:\n")

if start == "END":
    print("You have no choice, enter START")
    while start != "START":
        start = input()
        if start == "START":
            break
        print("You have no choice, enter START")

print("-"*50 + "Go little rock star!" + "-"*52)
print("We have two unique buckets: one holds 5 liters of liquid, and the other - 3 liters.")
first_bucket = 5
second_bucket = 3
trash = 0
moves = """------------------------------------------------------
- To transfer from the first bucket to the second bucket, enter 1
- To transfer from the second bucket to the first bucket, enter 2
- Pour the water out of the bucket , enter 3
- Add water to the bucket, enter 4
"""
print(moves)
action = int(input("Your move?:"))
while first_bucket != 4 and second_bucket != 4:
    while action == 1:
        if first_bucket >= second_bucket == 0:
            second_bucket += first_bucket
            if second_bucket > 3:
                second_bucket = 3
            first_bucket = first_bucket - second_bucket
        elif first_bucket >= second_bucket:
            trash = 3 - second_bucket
            first_bucket -= trash
            second_bucket += first_bucket
            if second_bucket > 3:
                trash = 5 - second_bucket
                second_bucket = 3
        elif second_bucket >= first_bucket:
            second_bucket += first_bucket
            if second_bucket > 3:
                trash = 5 - second_bucket
                second_bucket = 3
            first_bucket = first_bucket - trash
        if first_bucket == 4 or second_bucket == 4:
            break
        print(f"What's next?\n\nFirst bucket -- {first_bucket}\nSecond bucket -- {second_bucket}")
        print(moves)
        action = int(input("Your move?:"))

    while action == 2:
        if second_bucket >= first_bucket:
            trash = second_bucket
            first_bucket += second_bucket
            second_bucket -= trash
            if first_bucket > 5:
                first_bucket = 5
        if first_bucket == 4 or second_bucket == 4:
            break
        print(f"What's next?\nFirst bucket -- {first_bucket}\nSecond bucket -- {second_bucket}")
        print(moves)
        action = int(input("Your move?:"))

    while action == 3:
        print("First or Second bucket?")
        bucket = int(input("Enter 1 or 2:"))
        if bucket == 1:
            first_bucket = 0
        else:
            second_bucket = 0
        if first_bucket == 4 or second_bucket == 4:
            break
        print(f"What's next?\nFirst bucket -- {first_bucket}\nSecond bucket -- {second_bucket}")
        print(moves)
        action = int(input("Your move?:"))

    while action == 4:
        if first_bucket == 5 and second_bucket == 3:
            print("The buckets are already full")
            print(f"What's next?\nFirst bucket -- {first_bucket}\nSecond bucket -- {second_bucket}")
            print(moves)
            action = int(input("Your move?:"))
        else:
            print("First or Second bucket?")
            bucket = int(input("Enter 1 or 2:"))
            if bucket == 1:
                first_bucket = 5
            else:
                second_bucket = 3
        if first_bucket == 4 or second_bucket == 4:
            break
        print(f"What's next?\nFirst bucket -- {first_bucket}\nSecond bucket -- {second_bucket}")
        print(moves)
        action = int(input("Your move?:"))
print("-"*55 + "YOU WIN" + "-"*55)
if first_bucket == 4:
    print(f"First bucket -- {first_bucket}")
else:
    print(f"Second bucket -- {second_bucket}")
