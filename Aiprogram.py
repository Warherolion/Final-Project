# Ai programming for monopoly game

from Main import players, property, chanceCards, CommunityChest, settings, dice_roll
import random
# All the AI easy functions 

aiPlayerList = []





def buy_rand():
    random.randint(0, len(property))

def Ai_easy(propertyTotal):
    print("The Ai is going now please wait....")
    for x in range(settings[2]):
        die1, die2, total1 = dice_roll()
        propertyTotal += total1
        print(propertyTotal)
        aiPlayerList[x]["playerLocation"] = property[propertyTotal]
        print(property[propertyTotal])
        print(aiPlayerList[x]["PlayerLocation"])
        return propertyTotal

propTotal = 0
for PlayerAi in range(settings[2]):
    aiPlayerList.append(
        {
        "AiName": PlayerAi,
        "money": settings[4],
        "properties": [],
        "railroads": [],
        "inJail":   False,
        "PlayerLocation": property[propTotal]
         }
    )
propTotal = Ai_easy(propTotal)



