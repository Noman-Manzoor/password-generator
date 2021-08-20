# this project guess the number whether they are equaql or not
print("||<<||>>>        NUMBER GUESSING GAME         <<<||>>||")
import random
randomNo = random.randint(1,100)

def checking_equality():
    while randomNo > 0:
        user_enter = int(input("Enter your favourite number: "))
        if user_enter > randomNo:
            print("You enterd the number that is greater than the computer selected number.")
            print("Because-------")
            print(f"Computer guess the number {randomNo} while you enterd the number {user_enter}.")
            
        elif user_enter < randomNo:
            print("You enterd the number that is smaller than the computer selected number.")
            print("Because-------")
            print(f"Computer guess the number {randomNo} while you enterd the number {user_enter}")
        else:
            print("You enterd the number that is equal than the computer selected number.")
            print("Because-------")
            print(f"Computer gussess the number {randomNo} while you enterd the number {user_enter}.")
            break

checking_equality()
print("GOOD BYEE!!")