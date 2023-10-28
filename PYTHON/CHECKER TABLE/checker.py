#i defined "O" to be playable spot while "X" is not playable spot

a = int(input("size: "))

for i in range(a):
   for j in range(a):
      if (i+j)%2 == 0:
         print("X", end="")
      else:
         print("O", end="")
   print(" ") #new line
