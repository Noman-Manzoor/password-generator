print("||>>>>>>>  DICE STIMULATOR  <<<<<<<||")
print("This will generate the different dice with every time execution of programm")
import random
roll = input("Do u want to dice? ")

while roll == "yes" or roll == "y":
    print("Rollinng the dicces..................\nThe values are ...............")
    randNo = random.randint(1,7)
    if randNo == 1:
        print('*')
    elif randNo == 2:
        print("* *")

    elif randNo == 3:
        print("* * *")

    elif randNo == 4:
        print("* * * *")

    elif randNo == 5:
        print(" * * * * *")

    else :
        print("* * * * * *")
    roll = input("Do u want to dice? ")
print("Good luck!!!!!!!!!!!!")
