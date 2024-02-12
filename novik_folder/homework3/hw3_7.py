# just for fun, I'm not sure if it's a correct solution or not

#number = input('Enter your 4 digit number \n')
#print("Digit in thousands position is", number[0])
#print("Digit in hundredth position is", number[1])
#print("Digit in tenths position is", number[3])
#print("Digit in units position is", number[4])


entered_number = int(input('Enter your 4 digit number \n'))
units = entered_number % 10
tenth = (entered_number // 10) % 10
hundredth = (entered_number // 100) % 10
thousands = (entered_number // 1000) % 10
print(f"единицы = {units}")
print(f"десятки = {tenth}")
print(f"сотни = {hundredth}")
print(f"тысячи = {thousands}")