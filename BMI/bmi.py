#bmi = weight(kg)/height^2 (cm)

weight = float(input("Weight : "))
height = int(input("Height : "))
height = height/100

print(weight/height**2)