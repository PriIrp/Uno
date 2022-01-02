#Start with turns
#Withdraw Cards
#Declare cards to AI
#Give each person a turn
#Make the cards work 
    #Use comparative get() logic to check for legal move - Call Pri. He big-brain
suits = ["Red", "Yellow", "Blue", "Green"]
x = 0

def playPlusCards(card, player, d):    #Makes the next player draw a certain number of cards. Player parameter for Player Object. 
    if card.value == -1:            #Uses the draw method of the player class
        player.draw(d)
        player.draw(d)
    elif card.suit == "4Plus":
        player.draw(d)
        player.draw(d)
        player.draw(d)
        player.draw(d)
    
def playColorChange(card):
    if card.suit == "Wild" or card.suit == "4Plus":
            c = int(input("""Choose the new color of the pile:
                                1. Red
                                2. Yellow
                                3. Blue
                                4. Green
                                Enter number of color: """))
            card.suit = suits[c-1]

def playSwitch(card, list):
    if card.value == -3:
        list.reverse()

def playSkip(card):
    if card.value == -2:
        global x
        x += 1

def checkLegal(card, obj):    
    if obj.suit == None:
        return True
    elif card.value == obj.value:
        return True
    elif card.suit == obj.value:
        return True
    elif card.suit == "Wild" or card.suit == "4Plus":
        return True
    else:
        print("Please play a legal move")
        return False

# def drawForLegal(player, deck):
#     pass

def specialCards(player, card, list, deck):
    playColorChange(card)
    playPlusCards(card, list[(x+1)%len(list)], deck)
    playSkip(card)
    playSwitch(card,list)

def checkWinner(player):
    player.isWinner()

def playerTurnGreeting(player):
    print(f"Hey {player.name}! It's you're move!")

def goodMove(player, card):
    print(f"\n{player.name} played {card.formatCard()}\n")

def game(player, pile, list1, deck):
    
    playerTurnGreeting(player)

    while True:
        card = player.chooseFromHand()
        if checkLegal(card, pile):
            player.removeCard(card)

            specialCards(player, card, list1, deck)

            pile = card
            
            if card.value >= 0:
                goodMove(player, card)
                
            global x
            x += 1
            break
        else:
            decision = input('''Would you like to choose another card from your hand, or draw a card?
1. Chose from Hand
2. Draw''')
            if decision == "1":
                pass
            elif decision == "2" or decision == "":
                pass
                #Repeated draw mechanic


        



        
        
#Pri, Tan

    

#Done: 
#Make a pile 

#Not done:
#Take input player
#Check legal
    #If legal, delete that card from hand and make that top of pile

    #if not Legal, ask to choose a new card
        #if not card is legal in hand, draw from deck. 
            #Each draw is auto-checked from legality before it is added to the hand. 
#End turn
