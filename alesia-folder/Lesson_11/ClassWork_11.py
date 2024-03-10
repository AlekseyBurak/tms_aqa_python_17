"""
'r' open for reading (default)
'w' open for writing, truncating the file first
'x' create a new file and open it for writing
'a' open for writing, appending to the end of the file if it exists
'+' open a disk file for updating (reading and writing)
"""

# try:
#     my_file = open("test.txt", "a")
#     for index in range(1, 6):
#         my_file.write(f"{index} -- I'm text\n")
# finally:
#     my_file.close()
#
# with open("test.txt", "r") as f:
#     for line in f:
#         print(line)

# with open("test.log", "a") as f:
#     for index in range(100):
#         f.write(f"{index} -- I'm some text. \n")


# DEBUG

def func(a, b):
    return a / b

for a, b in (
        (1, 2),
        (3, 4),
        (5, 0)
):
    print(a, b)
    sum1 = a + b
    prod = a * b
    print(sum1, prod)
    # breakpoint()
    func(a, b + 1)

