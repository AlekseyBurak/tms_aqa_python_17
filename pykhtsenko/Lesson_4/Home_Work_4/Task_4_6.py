# посчитать количество часто встречаемых символов в предложении
text = input().lower()
a = 0
b = ""
for letter in text:
  if letter.isalpha():
    if a < text.count(letter):
      a = text.count(letter)
      b = letter
    elif a == text.count(letter) and letter not in b:
      b+= letter
print("".join(sorted(b)))
print(a)