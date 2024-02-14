# Example_1
lst = [1, 5, 2, 9, 2, 9, 1]
i = 0

while i < len(lst):
    count = lst.count(lst[i])

    if count == 1:
        print(lst[i])

    i += 1


# Example_2
lst = input("Enter a list of elements with a unique value: ").split()

new_list = []
i = 0

while i < len(lst):
    count = lst.count(lst[i])

    if count == 1:
        new_list.append(lst[i])

    i += 1

if len(new_list) == 1:
    print(f"The list contains one unique element: {new_list[0]}")
elif len(new_list) > 1:
    print(f"Alert: The list contains several unique elements: {", ".join(new_list)}")
else:
    print("There are no unique elements")
