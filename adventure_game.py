print("||||>>>>>>>>>>       ADVENTURE GAME        <<<<<<<<<<||||")
answer = input("Would you like to play game?(yes/No): ")
if answer == "yes":
    answer = input("You are on edge of the road. would you like to turn left or right?")
    if answer == "left":
        answer = input("THere is monster infront of you .would you like to run or attack?")
        if answer == "run":
            answer = input("Would you like to run back or not?")
            if answer == 'back':
                print("GOOD EFFORT TO SAVE YOUR LIFE.")  
            elif answer == 'no':
                print("WRONG DESICCION //// GAME OVER.")
        elif answer == 'attack':
            answer = input("Do u have weapon?")
            if answer == "yes":
                print("GAME OVER !! becz u can not beat the monster.")
            elif answer == 'no':
                print("GAME OVER ! YOU TOOK THE WRONG DESICION.")
    elif answer == "right":
        answer = input("You see a bike and plane in your way.which one will you pick up?(bike/plane): ")
        if answer == 'bike':
            print("GOOD DESICION TO SAVE YOURSELF.")
        elif answer == 'plane':
            answer = input("Do u know how to fly a plane?(yes/no): ")
            if answer == 'yes':
                print("GOOD EFFORT FOR ESCAPE.")
            elif answer == 'no':
                print("SERIOUS MISTAKE .YOU ARE IN DANGER. GAME OVER!!!!!!") 
            else:
                print("You choosed a wrong input.")
    else:
        print("INVALID CHOICE .THE GAME IS OVER.")

else:
    print("It's your own choice to play the game or not!!!")

print(">>>>>>>>>>>>>>>>>        Byeeeeeeee Byeeeeeeeeeeee          <<<<<<<<<<<<<<<<<<")