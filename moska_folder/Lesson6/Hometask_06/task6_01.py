# ввод sssaasss
#ввывод s6s6s6a2a2s6s6s6
# не понялаб как сделать чтобы не повторялись значения
word = input('input your word:\n')
quantity = ""
def check_litters(word):
    for i in word:
        if i not in quantity:
            print(f"{i}{word.count(i)}", end = '')

check_litters(word)