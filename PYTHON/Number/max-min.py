#this problem I define that can input as much as want. it will stop when type "STOP"

max = 0
min = 0

while True :
    number = input("input your number or 'STOP' to stop: ")
    if number == "STOP":
        break
    number = float(number)
    if number>max :
        max = number
    if number<min:
        min = number

print("max :", max)
print("min :", min)