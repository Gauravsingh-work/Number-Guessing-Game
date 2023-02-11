import random
a= random.randrange(1,20)
#print(a)
turn = 6
while turn > 0:
    turn -= 1  # for decrement of the turns
    usr = int(input("Guess your number b/w 1 to 20: "))
    if usr > a:
        print("Your gussed number is greater  then the Real Number")
        print("You have" , turn ,"Turn left")
        if turn == 0:
            print("You loose")
    elif usr < a:
        print("Your guessed number is less than the Real Number")
        print("You have", turn, "Turn left")
        if turn == 0:
            print("You loose the game")
    elif usr == a:
        print("You won the game")
        break
