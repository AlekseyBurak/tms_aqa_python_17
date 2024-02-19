#быки и коровы

import random
num = int(input())
digit1_n = num // 1000
digit2_n = num % 1000 // 100
digit3_n = num % 1000 % 100 // 10
digit4_n = num % 1000 % 100 % 10

num_guess = random.randrange(1000, 9999)
print(num_guess)

digit1_g = num_guess // 1000
digit2_g = num_guess % 1000 // 100
digit3_g = num_guess % 1000 % 100 // 10
digit4_g = num_guess % 1000 % 100 % 10

byk_counter = 0
if digit1_n == digit1_g:
    byk_counter == byk_counter +1
if digit2_n == digit2_g:
    byk_counter == byk_counter +1
if digit3_n == digit3_g:
    byk_counter == byk_counter +1
if digit4_n == digit4_g:
    byk_counter == byk_counter +1
print(f"{byk_counter} быков")

cow_counter = 0
if digit1_n == digit2_g or digit1_n == digit3_g or digit1_n == digit4_g:
    cow_counter == cow_counter +1
if digit2_n == digit1_g or digit2_n == digit3_g or digit2_n == digit4_g:
    cow_counter == cow_counter +1
if digit3_n == digit1_g or digit3_n == digit2_g or digit3_n == digit4_g:
    cow_counter == cow_counter +1
if digit4_n == digit1_g or digit4_n == digit3_g or digit4_n == digit2_g:
    cow_counter == cow_counter +1
print(f"{cow_counter} коров")

if cow_counter != 4 and byk_counter != 4:
    print("вы не угадали, попробуйте снова")
else:
    print("вы угадали")

if cow_counter != 4 and byk_counter != 4:
    num_guess1 = random.randrange(1000, 9999)
print(num)
print(num_guess1)


