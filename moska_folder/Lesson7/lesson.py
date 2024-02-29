#task1
def nastya(num:int):

    if num > 0:
        num1 = num // 10
        num2 = num % 10
        num_1 = num2 * 10
        num_2 = num1
        new_num = num_1 + num_2
        print(new_num)
    else:
        print('incorrect symbol')
        return nastya

nastya(num=89)

#task2
my_text = ['aa', 'aaa', 'aaaaaaa', 'aaaaaaaaaa']
text = filter(lambda x: len(x) > 5, my_text)
print(list(text))

