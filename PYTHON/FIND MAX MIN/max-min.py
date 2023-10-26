#this problem I define that can input as much as want. it will stop when type 000

max = 0
min = 0

while True :
    number = float(input("input your number : "))
    if number>max :
        max = number
    if number<min:
        min = number
    if number == 000:
        break
print("max :", max)
print("min :", min)