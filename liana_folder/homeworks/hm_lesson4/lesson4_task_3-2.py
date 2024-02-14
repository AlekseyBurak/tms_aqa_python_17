lst = input("Enter text in list: ")
print("Your list:", lst.split())
print("".join(lst))

# TODO ask a question about "".join(lst) and " ".join(lst)

# Answer of chat.gpt (I only use it for questions, I don't use it to generate code)
# Проблема здесь заключается в том, что метод input() возвращает строку, а не список.
# Поэтому, когда вы вызываете lst.split() после input(), вы разбиваете введенную строку на подстроки,
# но не создаете список.
#
# Вот исправленный код:
#
# # Ввод строки и преобразование её в список
# lst = input("Enter text in list: ").split()
#
# # Вывод списка на экран
# print("Your list:", lst)
#
# # Вывод списка как строки с пробелами между элементами
# print(" ".join(lst))
#
# Этот код сначала вводит строку, а затем сразу разбивает её на список при помощи метода split().
# После этого он выводит список на экран и также выводит строку,
# сформированную из элементов списка с использованием метода .join().
