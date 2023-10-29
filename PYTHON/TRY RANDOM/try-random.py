import random

for i in range(3):
    user = int(input("your number: "))
    ai = random.randrange(1,7)
    if user==ai:
        print(f"YOU ARE CORRECT, {user}={ai}")
        print("YOU ARE LUCKY")
        break
    else :
        print(f"YOU NOOB, {user}!={ai}")