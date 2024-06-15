#guess the number

import random

target = random.randint(1,100)

while True:
    userChoice = int(input("guess the target:"))
    if(userChoice == target):
        print("success:correct guess!!")
        break
    elif(userChoice < target):
        print("your number was too small.take a bigger guess...")
    else:
        print("your number was too big.take a smaller guess...")


print("------GAMEOVER------")
