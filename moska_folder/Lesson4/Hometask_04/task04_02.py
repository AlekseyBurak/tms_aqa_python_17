#2) Дан список: l=[‘Ivan’, ‘Ivanou’], и 2 строки: а=Minsk, с=Belarus. Напечатайте текст:
# “Привет, Ivan Ivanou! Добро пожаловать в Minsk Belarus”

l = ["Ivan", "Ivanou"]
l1 = (' '.join(l))
a = str("Minsk")
c = str("Belarus")
print(f"Привет, {l1}! Добро пожаловать в {a} {c}")
