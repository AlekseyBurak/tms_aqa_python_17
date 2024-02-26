# Дан список чисел, вывести все элементы списка, которые больше предыдущего элемента
#
#
# my_array = [1, 2, 5, 2, 3, 2]
# my_filter = filter(lambda x: my_array[x] < my_array[x-1], my_array)
# print(list(my_filter))

# зубчитый массив:
# my_zub_array = [1, 2, [3, 4, [5, 6], 7], [8, [9, [10]]]]


# задача про нового ученика
# height = [165, 163, 162, 160, 157, 157, 155, 154]
# vasya = int(input("Vaya's height: "))
# updeta_array = height.append(vasya)
# sotered_height = sorted(height, key=lambda x:x)
# print(sotered_height)
# print(sotered_height.index(vasya)+1)