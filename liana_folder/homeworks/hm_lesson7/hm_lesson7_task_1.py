print("-"*50 + "Go little rock star!" + "-"*52)
print("We have two unique buckets: one holds 5 liters of liquid, and the other - 3 liters.")
first_bucket = 5
second_bucket = 3
action = 0
bucket = 0
moves = """
    ------------------------------------------------------
    - To transfer from the first bucket to the second bucket, enter 1
    - To transfer from the second bucket to the first bucket, enter 2
    - Pour the water out of the bucket , enter 3
    - Add water to the bucket, enter 4
    """


def which_bucket():
    global bucket
    print("First or Second bucket?")
    bucket = int(input("Enter 1 or 2:"))

    if bucket == 1:
        return first_bucket
    elif bucket == 2:
        return second_bucket


def action1():
    global first_bucket, second_bucket

    if second_bucket > 0:
        space = 3 - second_bucket
        if space >= first_bucket:
            second_bucket += first_bucket
            first_bucket = 0
        elif space < first_bucket:
            first_bucket -= space
            second_bucket += space
    elif second_bucket == 0:
        second_bucket = first_bucket
        if second_bucket > 3:
            second_bucket = 3
        first_bucket -= 3
        if first_bucket < 0:
            first_bucket = 0

    return first_bucket, second_bucket


def action2():
    global first_bucket, second_bucket

    if first_bucket <= 2:
        first_bucket += second_bucket
        second_bucket = 0
    if first_bucket > 2:
        space = 5 - first_bucket
        if space >= second_bucket:
            first_bucket += second_bucket
            second_bucket = 0
        elif space < second_bucket:
            second_bucket -= space
            first_bucket += space

    return first_bucket, second_bucket


def action3():
    global first_bucket, second_bucket

    if which_bucket() == first_bucket:
        first_bucket = 0
        if first_bucket == 0:
            print("The bucket is already empty")
    else:
        second_bucket = 0
        if second_bucket == 0:
            print("The bucket is already empty")

    return first_bucket, second_bucket


def action4():
    global first_bucket, second_bucket

    if which_bucket() == first_bucket:
        first_bucket = 5
        if first_bucket == 5:
            print("The bucket is already full")
    else:
        second_bucket = 3
        if second_bucket == 3:
            print("The bucket is already full")

    return first_bucket, second_bucket


while first_bucket != 4:
    print(moves)
    print(f"What's next?\n\nFirst bucket -- {first_bucket}\nSecond bucket -- {second_bucket}")
    action = int(input("Your move?:"))
    if action == 1:
        action1()
    elif action == 2:
        action2()
    elif action == 3:
        action3()
    elif action == 4:
        action4()
