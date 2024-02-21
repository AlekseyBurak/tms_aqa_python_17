print(
 """
 Выберите операцию:
1. сложение
2. вычетание
3. умножение
4. деление
5. выход
"""
            )
def nastya(punkt:str, a1:int, a2:int):
      if punkt == '1':
            a1 = int(input('Введите 1 число:\n'))
            a2 = int(input('Введите 2 число:\n'))
            return(a1 + a2)
      elif punkt == '2':
            a1 = int(input('Введите 1 число:\n'))
            a2 = int(input('Введите 2 число:\n'))
            return(a1 - a2)
      elif punkt == '3':
            a1 = int(input('Введите 1 число:\n'))
            a2 = int(input('Введите 2 число:\n'))
            return(a1 * a2)
      elif punkt == '4':
            a1 = int(input('Введите 1 число:\n'))
            a2 = int(input('Введите 2 число:\n'))
            if a2 > 0:
                  return(a1 / a2)
            else:
                  return("Impossible")
      elif punkt == '5':
            return('Bye')

punkt = input()
a1 = int()
a2 = int()

print(nastya(punkt, a1, a2))
