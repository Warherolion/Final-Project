# Ai programming for monopoly game

from Main import *
import random
# All the AI easy functions 

aiPlayerList = []

for PlayerAi in range(settings[2]):
    aiPlayerList.append(
        {
        "AiName": "AiPlayer" + PlayerAi,
        "money": settings[4],
        "properties": [],
        "railroads": [],
        "inJail":   False,
        "PlayerLocation": property[0]
         }
    )
def buy_rand():
    random.randint(0, len(property))

def Ai_easy():
    print("The Ai is going now please wait....")
    for x in range(settings[2]):
        die1, die2, total = dice_roll()
        aiPlayerList[x]["PlayerLocation"]+= total
        print(aiPlayerList[x]["PlayerLocation"])
# hello
        




