#Напишите программу которая удаляет пробел в начале и в конце строки

a = str(input("Input string with spaces at the start, middle and end of the line:\n"))
print("You can see line without spaces at the start and end of the line:\n" + (a.strip()))