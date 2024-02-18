#задача про ведра из Крепкого орешка- 3, вроде получилось решить, но
#но не могу понять, почему в конце print выдает несколько ведер, хотя цикл завершен и цель выполнена
#пойду смотреть Крепкий орешек -3

vedra = {"V3": 0, "V5": 0}

command = input("Press 1 if you want to fill up V3\n"
                "Press 2 if you want to fill up V5\n"
                "Press 3 if you want to fill up both buckets\n")

if command == "1":
    vedra["V3"] += 3
if command == "2":
    vedra["V5"] += 5
if command == "3":
    vedra["V5"] += 5
    vedra["V3"] += 3

print(vedra)

while vedra["V5"] != 4:
    command = input("Press 1 if you want to fill up V3\n"
                    "Press 2 if you want to fill up V5\n"
                    "Press 3 if you want to empty V3\n"
                    "Press 4 if you want to empty V5\n"
                    "Press 5 if you want to pour V3 into V5\n"
                    "Press 6 if you want to pour V5 into V3\n")

    x = 5 - vedra["V5"] #переменные x и y показывают максимально возмоный
    y = 3 - vedra["V3"] #отлив из ведра при переливе в одном из ведер

    if command == "1":
        vedra["V3"] = 3

    if command == "2":
        vedra["V5"] = 5

    if command == "3":
        vedra["V3"] = 0


    if command == "4":
        vedra["V5"] = 0


    if command == "5":
        vedra["V5"] += vedra["V3"]
        if vedra["V5"] <= 5:
            vedra["V3"] = 0

        if vedra["V5"] > 5:
            vedra["V3"] = vedra["V3"] - x
            vedra["V5"] = 5


    if command == "6":
        vedra["V3"] += vedra["V5"]
        if vedra["V3"] < 3:
            vedra["V5"] = 0
        if vedra["V3"] > 3:
            vedra["V3"] = 3
            vedra["V5"] = vedra["V5"] - y
    print(vedra)

else:
 print(f"{vedra}\n Good job!!! Bucket V5 got 4 litters, done")







