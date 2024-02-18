THREE_LITER_BUCKET_SIZE = 3
FIVE_LITER_BUCKET_SIZE = 5
EXPECTED_LITERS_COUNT = 4

three_liter_bucket = 0
five_liter_bucket = 0

user_input = input("Select 1 option: 1. Fill a 3l bucket, 2. Fill a 5l bucket: ")

while not user_input.isdigit() or (user_input != '1' and user_input != '2'):
    print("\nError: The input value should be digits: 1 or 2\n")
    user_input = input("Select 1 option: 1. Fill a 3l bucket, 2. Fill a 5l bucket: ")

if user_input == '1':
    three_liter_bucket += THREE_LITER_BUCKET_SIZE
else:
    five_liter_bucket += FIVE_LITER_BUCKET_SIZE

while five_liter_bucket != EXPECTED_LITERS_COUNT:

    print(f"\n3-liter bucket = {three_liter_bucket}")
    print(f"5-liter bucket = {five_liter_bucket}\n")

    user_input = input("Select 1 option:\n"
                       "1. Fill a 3l bucket,\n"
                       "2. Fill a 5l bucket,\n"
                       "3. Empty a 3l bucket,\n"
                       "4. Empty a 5l bucket,\n"
                       "5. Pour water from a 3l into a 5l bucket,\n"
                       "6. Pour water from a 5l into a 3l bucket: ")

    while not user_input.isdigit() or user_input not in ['1', '2', '3', '4', '5', '6']:
        print("\nError: The input value should be digits: 1, 2, 3, 4, 5, 6\n")
        user_input = input("Select 1 option:\n"
                           "1. Fill a 3l bucket,\n"
                           "2. Fill a 5l bucket,\n"
                           "3. Empty a 3l bucket,\n"
                           "4. Empty a 5l bucket,\n"
                           "5. Pour water from a 3l into a 5l bucket,\n"
                           "6. Pour water from a 5l into a 3l bucket: ")

    if user_input == '1':
        three_liter_bucket = THREE_LITER_BUCKET_SIZE
    elif user_input == '2':
        five_liter_bucket = FIVE_LITER_BUCKET_SIZE
    elif user_input == '3':
        three_liter_bucket = 0
    elif user_input == '4':
        five_liter_bucket = 0
    elif user_input == '5':
        five_liter_bucket += three_liter_bucket
        three_liter_bucket = 0
        if five_liter_bucket > FIVE_LITER_BUCKET_SIZE:
            three_liter_bucket = five_liter_bucket - FIVE_LITER_BUCKET_SIZE
            five_liter_bucket = FIVE_LITER_BUCKET_SIZE
    elif user_input == '6':
        three_liter_bucket += five_liter_bucket
        five_liter_bucket = 0
        if three_liter_bucket > THREE_LITER_BUCKET_SIZE:
            five_liter_bucket = three_liter_bucket - THREE_LITER_BUCKET_SIZE
            three_liter_bucket = THREE_LITER_BUCKET_SIZE

print(f"\nYou are winner! \n3-liter bucket = {three_liter_bucket} \n5-liter bucket = {five_liter_bucket}")
