import math
while True:
    try:
        codeNumberOnASCII = int(input("Please enter number from 0 to 255" + ' '))
        if codeNumberOnASCII < 0 or codeNumberOnASCII > 255:
            print('Repeat again')
        else:
            print("Your entered number number in ASCII is symbol", chr(codeNumberOnASCII))
        break
    except ValueError:
        print("PLease enter numbers")
