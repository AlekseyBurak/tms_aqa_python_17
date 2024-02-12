import math

a = int(input("\nВведи 4-значное число :"))
print("В этом числе:\nтысяч - " + str(a//1000)
      + "\nсотен - " + str(math.trunc((math.fmod(a, 1000)) // 100))
      + "\nдесятков - " + str(math.trunc((math.fmod(a, 100)) // 10))
      + "\nединиц - " + str(math.trunc(math.fmod(a, 10))))
