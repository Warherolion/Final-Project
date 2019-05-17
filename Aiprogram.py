# Ai programming for monopoly game

from Main import *
import random
# All the AI easy functions 

aiPlayerList = []
propLoc = 0
for PlayerAi in range(settings[2]):
    aiPlayerList.append(
        {
        "AiName": PlayerAi,
        "money": settings[4],
        "properties": [],
        "railroads": [],
        "inJail":   False,
        "PlayerLocation": propLoc
         }
    )
def buy_rand():
    buyEasy = random.randint(0, 1)
    return buyEasy

def Ai_easy():
    print("The Ai is going now please wait....")
    time.sleep(1)
    for x in range(settings[2]):
            buyEasy = buy_rand()
            die1, die2, total, snakeEyes = dice_roll()
            AiLoc = propLoc + total 
                if buyEasy == 1: 
                        if propertycheck == None: 
                        aiPlayerList[x]["properties"] = property[AiLoc]
                        aiPlayerList[x]["PlayerLocation"] = AiLoc
                        print("The Computer rolled a", die1,"and a", die2, "and landed on", property[AiLoc], "and bought it")  
                        if snakeEyes == True:
                                print("The computer also got Snake eyes! and gets to roll again")   
                                die1, die2, total, snakeEyes = dice_roll()
                                if buyEasy == 1: 
                                        if propertycheck == None: 
                                        aiPlayerList[x]["properties"] = property[AiLoc]
                                        aiPlayerList[x]["PlayerLocation"] = AiLoc
                                        print("The Computer rolled a", die1,"and a", die2, "and landed on", property[AiLoc], "and bought it")  
                                        elif propertycheck != None:
                                                print("The Computer rolled a", die1,"and a", die2, "and landed on", property[AiLoc], "which is owned by", propertycheck)   
                                                elif buyEasy == 0:
                                elif buyEasy == 0
                                        aiPlayerList[x]["PlayerLocation"] = AiLoc 
                                        print("The Computer rolled a", die1,"and a", die2, "and landed on", property[AiLoc], "and did not buy it")
                elif buyEasy == 0:
                        aiPlayerList[x]["PlayerLocation"] = AiLoc 
                        print("The Computer rolled a", die1,"and a", die2, "and landed on", property[AiLoc], "and did not buy it") 


Ai_easy()

