array = [1,5,2,9,2,9,1]
s = set()
for number in array:
    if number in s:
        s.remove(number)
    else:
        s.add(number)
print(f'Unique number: {s}')