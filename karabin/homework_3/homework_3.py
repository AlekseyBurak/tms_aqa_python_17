a = {
    'EUR' : 1,
    'CAD' : 0.75,
    'BYN' : 0.32
}

b = {
    'EUR' : 2,
    'CAD' : 1.23,
    'RUB' : 0.12
}

new_a = a.copy()
new_b = b.copy()

new_a.update(b)
new_b.update(a)

print(new_a)
print(new_b)