def calc(a, b):
    if isinstance(a, int) and isinstance(b, int):
        return  a + b
    else:
        return "Error"
 #
def test_1():
     if calc(3, 4) == 7:
         print("ok")
     else:
         print("not ok")

def test_2():
     if calc(3.0, 4) == "Error":
         print("ok")
     else:
         print("not ok")

def test_3():
     try:
        if calc(-4, "5", 6) =="Error":
            print("ok")
        else:
             print("not ok")
     except:
         print("not ok")


def test_4():
     if calc(4, (1, 2)) == "Error":
         print("ok")
     else:
         print("not ok")



# test_1()
# test_2()
test_4()