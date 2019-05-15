# Poker: 5-Card Draw Final 

# Name: Ibrahim Issa
# Date Last Modified: January 18th, 2019
# Class Code: ICS3U
# Project: Final Summative


#   Elevator Pitch

    # Main Data -   # Player vs. Bot, Bot makes decisions based on various factors in game
                    # DECK - list of all 52 cards in deck
                    # PLAYER, BOT - lists for each player's current hand
                    # PLAYER_CHIPS, BOT_CHIPS - current player's chips
                    # POT - current pot value
                    # Dictionary - various dictionaries used to translate ("Jack","Queen","King","Ace") into comparable numbers

    # deal() - deals cards to each player until they have 5 cards in hand.
    # bet() - allows players to either call, raise, all-in, or fold a bet.
    # discard() - players can discard up to 3 cards and then dealt the same amount back.
    # check_hand() - checks player's hand for high card, pair, two pair, three of a kind, straight, flush, full house, four of a kind, straight flush, and royal flush.
    # winner() - compares both players' final hands to decide the winner.
    # leaderboard() - posts leaderboard depending on amount of chips a player has.



#   Rules of the Game

    #   Each round, players are each dealt 5 cards face-down.
    #   Betting round starts; players can call, raise, fold, or all-in with their chips; each player starts with 100 chips; all chips go to the pot when played.
    #   After betting, players may choose to discard unwanted cards (up to 3 cards) and are dealt the discarded amount of cards face-down.
    #   After the discard, another round of betting begins.
    #   Players reveal their hands; best hand wins (Royal Flush, Straight Flush, Four of a kind, etc.) and winning player is rewarded the pot.
    #   In the case of a draw, the pot is split between both players.
    #   ACE card is considered the highest card.
    #   Game ends when one player is left with 0 chips or if there are no more cards left to deal; Player with the most chips wins the game.



import random
import time

# Deal cards

def deal(PLAYER,BOT):   # Deals cards until each hand has 5 cards

    while len(PLAYER) != 5:
        random_num = random.randint(0,len(DECK)-1)
                                    
        if DECK[random_num] != "-":
            PLAYER.append(DECK[random_num]) 
        
        del(DECK[random_num])
        DECK.insert(random_num,"-")
    
        
    while len(BOT) != 5:
        random_num = random.randint(0,len(DECK)-1)

        if DECK[random_num] != "-":
            BOT.append(DECK[random_num]) 
        
        del(DECK[random_num])
        DECK.insert(random_num,"-")
                                                                                      
    return PLAYER, BOT 


# discard cards

def discard(PLAYER,BOT):      # Discards number of cards from hand

    a,b,c,d,e,f,g,h,i,j = check_hand(BOT)
    
    if a != 0 or b != 0 or c != 0 or d != 0 or e != 0 or f != 0 or g != 0 or h != 0:        # bot checks hand before deciding to discard
        pass
    else:
        random_num1 = random.randint(1,2)
        
        for y in range(random_num1):

            while True:
            
                random_num2 = random.randint(0,len(BOT)-1)

                card = BOT[random_num2].split("-")

                if card[0] == "Jack":
                    card.remove("Jack")
                    card.insert(0,11)
                elif card[0] == "Queen":
                    card.remove("Queen")
                    card.insert(0,12)
                elif card[0] == "King":
                    card.remove("King")
                    card.insert(0,13)
                elif card[0] == "Ace":
                    card.remove("Ace")
                    card.insert(0,14)

                if int(card[0]) != i:                # ensures that the bot does not discard a pair if he has one in hand

                    del(BOT[random_num2])
                    break
                
                else:
                    pass

        print("\nBot discarded",random_num1,"card(s).")

    #-----------------------------------------------------
    z = False

    while z == False:
        
        discard_card = input("\n   Do you wish to discard? (y/n): ")

        if discard_card in ("no","n","No","NO","N"):
            
            z = True

        elif discard_card in ("yes","y","Yes","YES","Y"):
        
            x = False
                
            while x == False:

                try:
                    disc_num = int(input("\n   Enter number of cards: "))
                    
                    if disc_num > 3 :
                        print("\n Invalid Input. Can only discard up to 3 cards.")

                    elif disc_num == 0:
                        print("\n Invalid Input.")

                    else:
                        x = True
                    
                except ValueError:
                    
                    print("\n Invalid Input.")
  
            for x in range(disc_num):

                y = False
            
                while y == False:
                
                    try:

                        print("\n Current Hand: ",PLAYER)
                        card = input("\n   Enter card (ex. 2-S, King-D, etc.): ")
                        del(PLAYER[PLAYER.index(card)])
                        y = True

                    except:
        
                        if card not in PLAYER:
                            print("\n Invalid. Card not in hand.")    
                 
            print("\n Card(s) Discarded.")
            
            z = True

        else:
            print("\n Invalid Input.")

        deal(PLAYER,BOT)

    
# Betting

def bet(BOT_CHIPS,PLAYER_CHIPS,POT,BOT):        # Call, Raise, Fold, or All-in

    time.sleep(2)
    
    a,b,c,d,e,f,g,h,i,j = check_hand(BOT)       # Bot checks hand before betting

    if a != 0 or b != 0 or c != 0 or d != 0:    # if hand is one of the following, bot is all-in
        bot_bet = 100
        print("  -- Bot is going ALL-IN!-- \n")
        POT += BOT_CHIPS
        BOT_CHIPS = 0

    elif  e != 0 or f != 0 or g != 0:      # else, bot bets randomly
        
        bot_bet = random.randint(20,30)

        print("Bot has bet '",bot_bet,"' \n")
        BOT_CHIPS -= bot_bet
        POT += bot_bet
 
    else:
        bot_bet = random.randint(10,20)

        print("Bot has bet '",bot_bet,"' \n")
        BOT_CHIPS -= bot_bet
        POT += bot_bet

    print("Pot: ",POT,"\n"  )

    #-------------------------------------------------

    invalid = True

    while invalid == True:
            
        player_bet = input("  Call, Raise, Fold, or All-In? ")

        if player_bet in ("call","Call","CALL"):        # bets the same amount as the current bet

            if bot_bet < 100:
            
                PLAYER_CHIPS -= bot_bet
                POT += bot_bet
                print("\nPlayer has called for '",bot_bet,"'")
                break

            else:
                print("\n  --Player is going ALL-IN!-- \n")
                POT += PLAYER_CHIPS
                PLAYER_CHIPS = 0

                break

        elif player_bet in ("raise","Raise","RAISE"):         # raises bet by adding more chips to current bet
            
            print("\nCurrent chips: ",PLAYER_CHIPS,"\n")
            
            x = False
            
            while x == False:
                
                try:
                    raise_amount = int(input("  Enter amount to raise: "))

                    if raise_amount <= PLAYER_CHIPS:
                        
                        total = raise_amount + bot_bet
                        PLAYER_CHIPS -= total
                        POT += total
                        print("\n Player has raised: ",raise_amount)
                        print("\n Player has bet: ",total)

                        time.sleep(1)

                        if total > 50:           
                            
                            a,b,c,d,e,f,g,h,i,j = check_hand(BOT)               # if raise is high, bot checks hand before making a decision

                            if a != 0 or b != 0 or c != 0 or d != 0 or e != 0 or f != 0 or g != 0:     # if hand is good, bot calls the raise
                                print("Bot has called for '",total,"' \n")
                                BOT_CHIPS -= total - bot_bet
                                invalid = False

                            else:                                   # else, bot folds and player wins
                                bot_bet = "fold"
                                invalid = False
                        
                        else:
                            print("\nBot has called for '",total,"' \n")
                            BOT_CHIPS -= total - bot_bet
                            POT += total - bot_bet
                            invalid = False
                    
                        x = True
                        
                    else:
                        print("\nInvalid Input. Not enough chips.\n")
                    
                except:
                    
                    print("\nInvalid Input. \n")          

            break

        elif player_bet in ("fold","Fold","FOLD"):
            invalid = False
            pass

        elif player_bet in ("all-in","All-in","All-In","ALL-IN"):
            
            print("\n  --Player is going ALL-IN!-- ")
            POT += PLAYER_CHIPS
            PLAYER_CHIPS = 0

            time.sleep(1)

            if BOT_CHIPS != 0:

                if a != 0 or b != 0 or c != 0 or d != 0 or e != 0 or f != 0 or g != 0:

                    print("\n  --Bot is going ALL-IN!-- ")
                    POT += BOT_CHIPS
                    BOT_CHIPS = 0
            
                else:
                    bot_bet = "fold"
                    invalid = False
            
            invalid = False

        else:
            print("\nInvalid Input. \n")

     
    print("\nPot: ",POT)

    return BOT_CHIPS, PLAYER_CHIPS, POT, player_bet, bot_bet



def check_hand(hand):   

    card_value = []     # list of card values 
    card_suit = []      # list of card suits
    
    royal_flush = 0
    straight_flush = 0
    four_of_a_kind = 0
    full_house = 0
    flush = 0
    straight = 0
    three_of_a_kind = 0
    two_pair = 0
    pair = 0
    
    card_1 = hand[0].split("-")     # Split hand into seperate lists , one for card value, and one for card suit
    card_value.append(card_1[0])
    card_suit.append(card_1[1])
    card_2 = hand[1].split("-")
    card_value.append(card_2[0])
    card_suit.append(card_2[1])
    card_3 = hand[2].split("-")
    card_value.append(card_3[0])
    card_suit.append(card_3[1])
    card_4 = hand[3].split("-")
    card_value.append(card_4[0])
    card_suit.append(card_4[1])
    card_5 = hand[4].split("-")
    card_value.append(card_5[0])
    card_suit.append(card_5[1])


    Dict = {            # Used to compare Jack, Queen, King, and Ace as numerical values

        "Jack":"11",    
        "Queen":"12",
        "King":"13",
        "Ace":"14"
        }
    
    while ("Jack" in card_value) or ("Queen" in card_value) or ("King" in card_value) or ("Ace" in card_value):     # Dictionary replaces worded cards with numerical numbers for
                                                                                                                    #   easy comparisons
        if "Jack" in card_value:
            card_value.insert(card_value.index("Jack"),Dict["Jack"])
            del(card_value[card_value.index("Jack")])
        if "Queen" in card_value:
            card_value.insert(card_value.index("Queen"),Dict["Queen"])
            del(card_value[card_value.index("Queen")])
        if "King" in card_value:
            card_value.insert(card_value.index("King"),Dict["King"])
            del(card_value[card_value.index("King")])
        if "Ace" in card_value:
            card_value.insert(card_value.index("Ace"),Dict["Ace"])
            del(card_value[card_value.index("Ace")])

    card_value[0] = int(card_value[0])
    card_value[1] = int(card_value[1])
    card_value[2] = int(card_value[2])
    card_value[3] = int(card_value[3])
    card_value[4] = int(card_value[4])

    card_value.sort()

    high_card = max(card_value)

    counter = 0

    for card in card_value:             # counts card_value list for like cards and finds pairs, two pairs, three of a kind, and four of a kind
        count = card_value.count(card)

        if count == 4:
            four_of_a_kind = card
        if count == 3:
            three_of_a_kind = card
        if count == 2:
            pair = card
            counter += 1

    if counter == 4:
        two_pair = True

    for suit in card_suit:              # counts suits in card_suit and checks for flush
        count = card_suit.count(suit)

        if count == 5:
            flush = True

    if pair != 0 and three_of_a_kind != 0:
        full_house = True

    if (card_value[0])+1 == (card_value[1]):
        if (card_value[1])+1 == (card_value[2]):
            if (card_value[2])+1 == (card_value[3]):
                if (card_value[3])+1 == (card_value[4]):
                    straight = card_value[4]

    if straight != 0 and flush == True:
        straight_flush = card_value[4]

    if (straight != 0 and card_value[0] == 10 and flush == True):
        royal_flush = True

    return royal_flush, straight_flush, four_of_a_kind, full_house, flush, straight, three_of_a_kind, two_pair, pair, high_card




def winner(PLAYER,BOT, PLAYER_CHIPS, BOT_CHIPS):

    print("\n  Revealing Hands... \n")

    time.sleep(2)

    a,b,c,d,e,f,g,h,i,j = check_hand(PLAYER)            # checks the hand, a is greatest hand (Royal Flush), j is lowest hand (high card)

    player_hand = 0

    if a != 0:           
        player_hand = 10
        print("Player: ",PLAYER," - Royal Flush \n")
    elif b != 0:
        player_hand = 9
        print("Player: ",PLAYER," - Straight Flush \n")
    elif c != 0:
        player_hand = 8
        print("Player: ",PLAYER," - Four of a kind \n")
    elif d != 0:
        player_hand = 7
        print("Player: ",PLAYER," - Full House \n")
    elif e != 0: 
        player_hand = 6
        print("Player: ",PLAYER," - Flush \n")
    elif f != 0:
        player_hand = 5
        print("Player: ",PLAYER," - Straight \n")
    elif g != 0:
        player_hand = 4
        print("Player: ",PLAYER," - Three of a kind \n")
    elif h != 0:
        player_hand = 3
        print("Player: ",PLAYER," - Two Pair \n")
    elif i != 0:
        player_hand = 2
        print("Player: ",PLAYER," - Pair \n")
    elif j != 0:
        player_hand = 1
        print("Player: ",PLAYER," - High Card \n")


    k,l,m,n,o,p,q,r,s,t = check_hand(BOT)

    bot_hand = 0

    if k != 0:
        bot_hand = 10
        print("\nBot:   ",BOT," - Royal Flush \n")
    elif l != 0:
        bot_hand = 9
        print("\nBot:   ",BOT," - Straight Flush \n")
    elif m != 0:
        bot_hand = 8
        print("\nBot:   ",BOT," - Four of a kind \n")
    elif n != 0:
        bot_hand = 7
        print("\nBot:   ",BOT," - Full House \n")
    elif o != 0:
        bot_hand = 6
        print("\nBot:   ",BOT," - Flush \n")
    elif p != 0:
        bot_hand = 5
        print("\nBot:   ",BOT," - Straight \n")
    elif q != 0:
        bot_hand = 4
        print("\nBot:   ",BOT," - Three of a kind \n")
    elif r != 0:
        bot_hand = 3
        print("\nBot:   ",BOT," - Two Pair \n")
    elif s != 0:
        bot_hand = 2
        print("\nBot:   ",BOT," - Pair \n")
    elif t != 0:
        bot_hand = 1
        print("\nBot:   ",BOT," - High Card \n")

    p_win = 0
    b_win = 0
    draw = 0

    if player_hand > bot_hand:              # compares hands to determine winner
        p_win = True
    elif player_hand < bot_hand:
        b_win = True
        
    elif player_hand == bot_hand:

        if a>k or b>l or c>m or d>n or e>o or f>p or g>q or h>r or i>s:
            p_win = True
            
        elif k>a or l>b or m>c or n>d or o>e or p>f or q>g or r>h or s>i:
            b_win = True

        elif j>t:
            player_hand = 1
            p_win = True
            print("\n Draw, ",end="")

        elif t>j:
            bot_hand = 1
            b_win = True
            print("\n Draw, ",end="")

        else:
            draw = True

    if p_win == True:
        PLAYER_CHIPS += pot
        print("Player wins with '",Dictionary[player_hand],"'")
        
    elif b_win == True:
        BOT_CHIPS += pot
        print("Bot wins with '",Dictionary[bot_hand],"'")
        
    elif draw == True:
        PLAYER_CHIPS += pot//2
        BOT_CHIPS += pot//2
        print("Draw, Pot Split.")

    return p_win, b_win, draw, player_hand, bot_hand, PLAYER_CHIPS, BOT_CHIPS


def leaderboard(player_chips, bot_chips):       # prints current leaderboard (leader being player with the most chips)
    
    if player_chips >= bot_chips:

        print("\n \n [ LeaderBoard ] \n")

        print(" # 1 - Player: ", player_chips, "Chips")

        print("\n # 2 - Bot:  ",bot_chips, "Chips \n \n \n")

    else:

        print("\n \n [ LeaderBoard ] \n")

        print(" # 1 - Bot: ", bot_chips, "Chips")

        print("\n # 2 - Player: ",player_chips, "Chips \n \n \n")
    

# MAIN PROGRAM

PLAYER = []      # PLAYER'S HAND

BOT = []         # BOT'S HAND

PLAYER_CHIPS = 100      

BOT_CHIPS = 100 

POT = 0

Dictionary = {                      # used for final hand comparison 

            1:"High Card",
            2:"Pair",
            3:"Two Pair",
            4:"Three of a kind",
            5:"Straight",
            6:"Flush",
            7:"Full House",
            8:"Four of a kind",
            9:"Straight Flush",
            10:"Royal Flush",

            }


print("\n \n                                     POKER: 5-CARD DRAW \n \n")

print("""

        Rules of the Game:

        #   Each round, players are each dealt 5 cards face-down
        
        #   Betting round starts; players can call, raise, fold, or all-in their chips; each player starts with 100 chips; all chips go to the pot
        
        #   After betting, players may choose to discard unwanted cards (up to 3 cards) and are dealt the discarded amount of cards face-down
        
        #   Another round of betting begins
        
        #   Players reveal their hands; best hand wins (Royal Flush, Straight Flush, Four of a kind, etc.)
        
        #   In the case of a draw, the pot is split between both players
        
        #   ACE card is considered the highest card
        
        #   Game ends when one player has 0 chips or if there are no more cards left to deal; Player with the most chips wins
    

""")

time.sleep(2)

start = "yes"       

while start not in ("n","No","no","NO","N"):        # loops program for player to choose to play again

    start = input("Start game? (y/n): ")

    if start in ("y","yes","YES","Y","Yes"):

        print("\n -----------------------------------------------------------------------------")

        print("                               Game Started                             \n")

        while True:

            p_chips = 100
            b_chips = 100
            pot = 0
            round_count = 0

            DECK = ["2-S","3-S","4-S","5-S","6-S","7-S","8-S","9-S","10-S","Jack-S","Queen-S","King-S","Ace-S",
                    "2-C","3-C","4-C","5-C","6-C","7-C","8-C","9-C","10-C","Jack-C","Queen-C","King-C","Ace-C",        
                    "2-H","3-H","4-H","5-H","6-H","7-H","8-H","9-H","10-H","Jack-H","Queen-H","King-H","Ace-H",
                    "2-D","3-D","4-D","5-D","6-D","7-D","8-D","9-D","10-D","Jack-D","Queen-D","King-D","Ace-D"]

            leaderboard(p_chips,b_chips)

            while (DECK.count("-") < 42) and (p_chips > 0 and b_chips > 0):

                round_count += 1

                print("-- Round ",round_count,"-- \n \n")
                
                print("Dealing...\n \n")
                
                time.sleep(2)                       
                 
                PLAYER.clear()
                BOT.clear()

                p,b = deal(PLAYER,BOT)

                print("Current Hand: ",p,"\n")

                print("Pot: ",POT,"\n")

                print("Chips: ",p_chips,"\n ")

                print("----------------------------------------------------------------\n")

                pot = 0
                
                b_chips, p_chips, pot, p_bet, b_bet = bet(b_chips,p_chips,pot,b)

                if p_chips == 0 and b_chips == 0:
                    break
                
                if p_bet not in ("fold","Fold","FOLD") and b_bet not in ("fold","Fold","FOLD"):

                    time.sleep(1)
                    
                    discard(p,b)                        

                    print("\nCurrent Player Hand: ",p,"\n")

                    b_chips, p_chips, pot, p_bet, b_bet = bet(b_chips,p_chips,pot,b)

                    if p_chips == 0 and b_chips == 0:
                        break

                    if p_bet not in ("fold","Fold","FOLD") and b_bet not in ("fold","Fold","FOLD"):

                        p_win,b_win,draw,p_hand,b_hand,p_chips,b_chips = winner(p,b,p_chips,b_chips)

                    else:
                        if p_bet in ("fold","Fold","FOLD"):
                            print("\nPlayer folds. Bot Wins! \n")
                            b_chips += pot
                            
                        elif b_bet in ("fold","Fold","FOLD"):
                            print("\nBot folds. Player Wins! \n")
                            p_chips += pot

                else:
            
                    if p_bet in ("fold","Fold","FOLD"):
                        print("\nPlayer folds. Bot Wins! \n")
                        b_chips += pot
                        
                    elif b_bet in ("fold","Fold","FOLD"):
                        print("\nBot folds. Player Wins! \n")
                        p_chips += pot

                time.sleep(1)

                leaderboard(p_chips,b_chips)

                time.sleep(1)
                

            if DECK.count("-") > 42:
                
                print("\n No more cards... GAME OVER. \n")
                

            elif p_chips == 0 and b_chips == 0:
                
                p_win,b_win,draw,p_hand,b_hand,p_chips,b_chips = winner(p,b,p_chips,b_chips)


            if p_chips >= b_chips:

                print("\n \n { Final LeaderBoard } \n")
                print("   # 1 - Player: ", p_chips, "Chips")
                print("\n   # 2 - Bot:  ",b_chips, "Chips \n \n")
                print("PLAYER WINS!")

            else:

                print("\n \n { Final LeaderBoard } \n")
                print("   # 1 - Bot: ", b_chips, "Chips")
                print("\n   # 2 - Player: ",p_chips, "Chips \n \n")
                print("BOT WINS!")
                
            while True:

                game = input("\n Play Again? (y/n): ")

                if game in ("y","n"):
                    break
                else:
                    print("\n Invalid Input.")

            if game in ("y","yes","YES","Yes"):
                continue
            
            else:
                print("\n Thanks for playing.")
                start = "no"
                break

    elif start in ("n","N","No","NO","no"):
        
        print("\n Ok...Bye...")
        break

    else:

        print("\n Invalid Input. \n")
