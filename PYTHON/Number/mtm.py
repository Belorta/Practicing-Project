#min to max and max to min
list = []

while True:
    number = int(input("input int: "))
    if number >= 0:
        list.append(number)
    else:
        break
a=sorted(list)
b=sorted(list, reverse=True)
#list.sort(), list.reverse() can use this instead.
print("Min to Max :", a)
print("Max to Min :", b)