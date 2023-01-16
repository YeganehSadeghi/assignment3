#tas - play :)
import random

tas = random.randint(1, 6)

while True :
    if tas == 6 :
        tas1 =random.randint(1, 6)
        tas2 = random.randint(1, 6)
        print("tas comes 6 go twice","first time =", tas1 ,"secend time =", tas2)
        break
    if    1<= tas <=5 : 
        print ("tas number is=", tas)
        break