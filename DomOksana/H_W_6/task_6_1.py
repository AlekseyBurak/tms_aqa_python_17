print("""HomeWork 6 Task 1: 
На вход подается строка, например, "cccbba" результат работы программы - строка “c3b2a" """)
#функция
def f_task(stroka: str):
    s_rez = ""
    kol = 1
    for i in range (len(stroka)-1):
        if stroka [i] == stroka [i+1]:
            kol += 1
        else:
            if kol > 1:
                s_rez += stroka[i] + str(kol)
            else:
                s_rez += stroka[i]
            kol = 1
        if i == len(stroka) - 2:
            if stroka[i] == stroka[i+1]:
                s_rez += stroka[i] + str(kol)
            else:
                s_rez += stroka[i+1]
    return s_rez
#задача
s = str(input("Введите строку: "))
print(f"Результат: {f_task(s)}")
