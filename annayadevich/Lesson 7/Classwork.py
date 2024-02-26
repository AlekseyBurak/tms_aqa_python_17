


#Про урок физкультуры задача
def sorted_height():
    all_height_from_class = [165, 163, 162, 160, 157, 157, 155, 154]
    petya_height = 162
    index_to_insert = all_height_from_class.index(petya_height) + 1
    all_height_from_class.insert(index_to_insert, petya_height)
    print(all_height_from_class)

sorted_height()



# def reverse_number(number: int) -> int:
#
#     if number < 0:
#         print("Positive")
#         return False
#     else:
#         list_num = list(str(number))
#         list_num.reverse()
#         reverse_int = int(''.join(list_num))
#         print(reverse_int)
#         return reverse_int
# #
# # reverse_number(9798)
#
# my_str_list =['hdd', '5', 'giugigigi', 'hiugug434']
# my_filtered_lambda = filter(lambda x: len(x) < 5, my_str_list)
# print(list(my_filtered_lambda))

