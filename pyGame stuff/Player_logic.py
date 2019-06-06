import time
# Allows for access to the settings file and drops values into a list

settings = []
with open("settings.txt") as file:
    for line in file:
        line = line.split(":")
        line = line[1]
        line = line.rstrip("\n")
        line = line[1:]
        line = line.split(" ")
        try:
            for x in range(len(line)):
                line[x] = int(line[x])
            line = (line[0], line[1])
        except:
            line = line[0]
            settings.append(line)
file.close()

settingsCheck = open("settings.txt", "r")
settingsSaved = False
if "MonoSet1-1" in settingsCheck.read():
    settingsSaved = True
















































































































players = []

playerMoveCount = []


# Error checking for inputs file stored as a function


def inputs(line, typeinp=None, start=None, end=None):
    while True:
        string = input(line)
        if typeinp != None:
            try:
                if typeinp == "string":
                    string = str(string)
                elif typeinp == "integer":
                    string = int(string)
                if start != None and end != None:
                    while not (string >= start and string <= end):
                        print("Please input a number between", str(start) + "-" + str(end))
                        string = int(input(line))
                break
            except:
                print("Please input a", typeinp)
        else:
            break
    return string


def playerChange():
    print("Next Player")
    print("***************************************")
    print("*")
    print("*")
    print("*")
    print("*")
    print("***************************************")
# Settings file, if user chooses to run setup this is all the setup questions


def gameSettingsSetup():
    settingsCheck = open("settings.txt", "r")
    print("Lets setup")
    # Int Setup questions
    numPlayers = str(inputs('How many real players are playing: ', "intger"))
    numAIplayers = str(inputs('How many AI players will be playing?: ', "integer"))
    if numAIplayers != "0":
        AILevel = str(inputs("What AI difficulty level would you like? (Easy, Normal, Hard): "))
        while True:
            if AILevel == "Easy" or AILevel == "Normal" or AILevel == "Hard":
                startingMoney = str(inputs("How much money does everyone start with? Max: 10 000 (Keep in mind "
                                           "this does not affect the property prices) ", "integer", 100, 10000))

                for i in range(int(numPlayers)):
                    name = input("What is the players name? ")
                    players.append({"playerName": name, "money":startingMoney, "properties": [], "railroads": []})

                break
            else:
                print("Please enter a valid input (make sure to capitalize the first letter)")
                AILevel = str(inputs("What AI difficulty level would you like? (Easy, Normal, Hard): "))

    elif numAIplayers == "0":
        startingMoney = str(inputs("How much money does everyone start with? Max: 10 000 (Keep in mind "
                                   "this does not affect the property prices) ", "integer", 100, 10000))

        for i in range(int(numPlayers)):
            name = input("What is the players name? ")
            players.append(name)

    print("Alright the setup is complete, Your game will start now....")
    time.sleep(1)

    # sends over the settings into the text file as well as monoset check
    if "MonoSet1-1" in settingsCheck.read():
        with open("settings.txt", "w") as file:
            file.write("MonoSet1-1: true" + "\n")
            file.write("numPlayer: " + numPlayers + "\n")
            file.write("numAIplayer: " + numAIplayers + "\n")
            file.write("AI Level: " + AILevel + "\n")
            file.write("startingMoney: " + startingMoney + "\n")
            file.close()

    return settingsCheck, players

