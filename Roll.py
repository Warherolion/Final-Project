# Calls either chance or community function to pick a random card and give it to the player

            ChanceCardPick = chancePickUp()

            CommunityCardPick = communityPickUp()

            # property owned check, sees if anyone owns the property and returns either none or the playerName

            def is_property_owned(property_name):
                for p in players:
                    if property_name in p['properties']:
                        return p['playerName']  # Returns the owner of property
                    else:
                        for a in aiPlayerList:
                            if property_name in a['properties']:
                                return a['AiName']  # Returns the owner of property
                return None

            

            time.sleep(1)
            pd = property.index(property[total])

            players[0 + x]["PlayerLocation"] += pd
    
            player_update = players[0 + x]["PlayerLocation"]

            # MoveTotal = players[0 + x]["PlayerLocation"]
            # print(MoveTotal)
            print("You rolled a", die1, "and a", die2, "you move forward",total, "steps \n")

            time.sleep(1)

            print("You landed on", property[player_update] + "\n")

            time.sleep(1)

            if property[player_update] == "Community Chest" or property[player_update] == "Chance":

                if property[player_update] == "Community Chest":

                    print(CommunityChest.index(CommunityCardPick))

                    print("The card you picked states", CommunityCardPick, "\n")

                elif property[player_update] == "Chance":

                    print(chanceCards.index(ChanceCardPick))

                    print("The card you picked states", ChanceCardPick)

                else:

                    print("Something went wrong, sorry")

            

            elif property[player_update] != "Community Chest":

                # checks if the user landed on income tax and will deduct it from their money

                if property[player_update] == "Income Tax":

                        print("You have to pay", propertyPrice[player_update])

                        money = int(players[x]["money"])

                        money -= propertyPrice[player_update]

                        print("You now have", money, "dollars \n")

                elif property[player_update] != "Income Tax":   

                    if property[player_update] != "Chance":

                        # Checks if any one owns the property

                        propertycheck = is_property_owned(property[player_update])

                        # if the property check results in a player name it will state that name

                        if propertycheck != None:


                            print("This property is owned by", propertycheck)

                        # checks if no one owns the property and is not on jail

                        elif propertycheck == None and property[player_update] != "jail/Just Visiting":

                            # prints the price of the property as long as it costs more than 0

                            if propertyPrice[player_update] > 0:

                                print("It costs " + str(propertyPrice[player_update]) + " dollars  ")

                                propertyBuyChoice = str(input("Do you want to buy this property? " + "\n"))

                                if propertyBuyChoice == "y" or propertyBuyChoice == "Y":

                                    if int(players[0 + x]["money"]) > propertyPrice[player_update]:

                                        print("You have", players[0 + x]["money"], "dollars \n")

                                        buyCheck = input(

                                            "You have enough money to buy this property, are you sure you want to buy it?: \n")

                                        if buyCheck == "y" or buyCheck == "Y":

                                            money = int(players[0 + x]["money"])

                                            money -= int(propertyPrice[player_update])

                                            players[0 + x]["properties"] = property[player_update]

                                            print("You now own", property[player_update] + "\n")

                                            time.sleep(2)
        
                                        elif buyCheck == "n" or buyCheck == "N":
        
                                            print("Ok Buy canceled... \n")
        
                                        else:
        
                                            print("Please enter either a n or y ")
        
                                    elif players[x]["money"] < propertyPrice[player_update]:
        
                                        print("You do not have enough money to buy this property")
                                        playerChange()
                                    elif players[x]["money"] == 0:
                                        print("Boi you are broke, you can't buy anything \n")
                                        playerChange()
                                elif propertyBuyChoice == "n" or propertyBuyChoice == "N":

                                    print("Alright")

                                else:
                                    print("Please input either y or n")
                                    propertyBuyChoice = str(input("Do you want to buy this property? " + "\n"))