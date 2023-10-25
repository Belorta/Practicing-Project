#C->F, F->C

temperature = float(input("Your temperature : "))
unit = str(input("Celsius or Fahrenheit : "))

if unit == "Celsius" :
    CtoF = (temperature*9/5)+32
    print(CtoF)
else :
    FtoC = (temperature-32)*(5/9)
    print(FtoC)