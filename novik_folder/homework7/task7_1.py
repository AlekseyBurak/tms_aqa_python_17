#def func(user_enter: int) -> int:
#    if user_enter < 0:
#        print("not allowed")
#    else:
#        list_number = list(str(user_enter))
#        list_number.reverse()
#        reverse_int = int(''. join(list_number))
#      print(reverse_int)
#        return reverse_int

#func(809)

my_str_list = ["aaaa", "bbbbhhhhh", "ccjjjjjjjj"]
my_filer = filter(lambda x: len(x) < 5, my_str_list)
print(list(my_filer))

height_of_people = [165, 163, 162, 157, 157, 155, 154]
height_of_petya = int(input("Enter height of Petya \n"))
more_height = filter(lambda height: height >= height_of_petya, height_of_people)
less_height = filter(lambda height: height < height_of_petya, height_of_people)
new_list = list(more_height)
new_list.append(height_of_petya)
list_less_height = list(less_height)
for elements in list_less_height:
    new_list.append(elements)
print(new_list)
