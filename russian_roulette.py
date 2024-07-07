from random import randint
import time
num_to_die = randint(1, 6)
shots_shot = 0




print("The Gun is loaded. Make Your Move.")
time.sleep(1)
# Game Loop
active = True
while active == True:
    game_over = False
    
    while True:
        #Player Turn Start
        a = input("Shoot Yourself, the Enemy, or Spin the Cylinder?\n")
        if a == "Myself":
            shots_shot += 1
            print("*You turn the gun on yourself*")
            time.sleep(3)
            if shots_shot == num_to_die:
                print("*BANG!!!*")
                print("You Lose.")
                game_over = True
            else:
                print("*click*")
                print("You Lived. For Now.")
                break
        elif a == "The Enemy":
            shots_shot += 1
            print("*You turn the gun to the enemy*")
            time.sleep(3)
            if shots_shot == num_to_die:
                print("*BANG!!!*")
                print("You Won.")
                game_over = True
            else:
                print("*click*")
                break
        elif a == "Spin the Cylinder":
            print("*You spin the cylinder*")
            num_to_die = randint(1, 6)
            print("*wssssshhhhhhh*")
            shots_shot = 0
            break
        else:
            print("Input unclear")

    #CPU Turn
    time.sleep(1)
    print("ENEMY'S TURN")
    decision = randint(1,3)
    if decision == 1:
        print("*He turns the gun on you*")
        time.sleep(3)
        shots_shot += 1
        if shots_shot == num_to_die:
            print("*BANG!!!*")
            print("You Lose.")
            game_over = True
        else:
            print("*click*")
            print("You Lived. For Now.")
    elif decision == 2:
        print("*He turns the gun on himself*")
        time.sleep(3)
        shots_shot += 1
        if shots_shot == num_to_die:
            print("*BANG!!!*")
            print("You Won.")
            game_over = True
        else:
            print("*click*")
    elif decision == 3:
        num_to_die = randint(1, 6)
        shots_shot = 0
        print("*He spins the cylinder*")
        print("*wssssshhhhhhh*")

    if game_over == True:
        break