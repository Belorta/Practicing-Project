a = int(input("row: "))
b = int(input("column: "))

for i in range(b-1):
    if i == 0:
        print("X"*a)
    if i == b-2:
        print("X"*a)
    else:
        print("X", " "*(a-4), "X")