#multiplication start at a, end at b

a = int(input())
b = int(input())

for i in range(a,b+1):
    for j in range(1,13):
        print(f"{a}x{j} = {a*j}")
        j+=1
    print(f"Multiplication of {a}")
    print("\n") #create blank space to separate each multiplication
    a+=1