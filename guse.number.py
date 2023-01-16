#play-guse-win :)

import random
counter=0
computer_number  = random.randint(0, 20)

while True:
    player_number = int (input("enter your guse number="))
    counter += 1  
    if player_number == computer_number :
        print ("you are win")
        print( "you are win with ",counter,"guse")
       
        break
    if computer_number < player_number :
        print("say smaller number")
    else :
        print("say bigger number")
        




