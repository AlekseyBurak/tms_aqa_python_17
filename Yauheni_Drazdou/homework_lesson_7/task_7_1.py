# задача про код цезаря

def encode(x, y) -> str:
    """
    This function encodes any string into a text
     in which every letter becomes different letter
    according to a particular step (Caesar code)
    :param x: inputted text
    :param y: step within which every letter will be substituted with
    another one based on alphabet location
    :return: coded text
    """
    l1 = list(x)
    l2 = []
    for i in l1:
        if ord(i) >= 123 - y:
            i = chr(ord(i) - (26 - y))
            l2.append(i)
        elif (ord(i) == 32 or ord(i) == 33 or ord(i) == 44 or
              ord(i) == 46 or ord(i) == 63):
            l2.append(i)
        else:
            i = chr(ord(i) + y)
            l2.append(i)
    print(''.join(l2))

a = str(input())
b = int(input())
encode(a, b)

def decode(x,y) -> str:
    """This function decodes any text based on Caesar's method
     according to inputted step
    :param x: inputted text
    :param y: step within which every letter will be decoded with
    another one based on alphabet location
    :return: decoded text
     """
    l1 = list(x)
    l2 = []
    for i in l1:
        if 97 <= ord(i) < 97 + y:
            i = chr(ord(i) + (26 - y))
            l2.append(i)
        elif (ord(i) == 32 or ord(i) == 33 or ord(i) == 44
              or ord(i) == 46 or ord(i) == 63):
            l2.append(i)
        else:
            i = chr(ord(i) - y)
            l2.append(i)
    print(''.join(l2))

a = str(input())
b = int(input())
decode(a, b)