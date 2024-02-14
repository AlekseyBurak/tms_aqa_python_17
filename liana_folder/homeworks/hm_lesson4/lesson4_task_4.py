lst = input("Enter 10 elements: ").split()
lst.insert(2, input('Enter new element: '))  # Is 2 or 3 index in 3 th position?
del lst[6]
print(f"Your list: {lst}")
