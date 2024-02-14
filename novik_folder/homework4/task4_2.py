#Дан список: l=[‘Ivan’, ‘Ivanou’], и 2 строки: а=Minsk, с=Belarus. Напечатайте текст: “Привет, Ivan Ivanou! Добро пожаловать в Minsk Belarus”

l = ['Ivan', 'Ivanou']
a = "Minsk"
c = "Belarus"
new_l = " ".join(l)
print(f'Привет, {new_l}! Добро пожаловать в {a} {c}')

