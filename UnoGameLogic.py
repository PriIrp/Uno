#Start with turns
#Withdraw Cards
#Declare cards to AI
#Give each person a turn
#Make the cards work 
    #Use comparative get() logic to check for legal move - Call Pri. He big-brain

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
                                4. Green"""))
            card.value = suits[c-1]

def playSwitch(card):
    if card.value == -3:
        people.reverse()

def playSkip(card):
    if card.value == -2:
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

def checkWinner(player):
    player.isWinner()

def playerTurnGreeting(player):
    print(f"Hey {player.name}! It's you're move!")

def goodMove(player, card):
    print(f"{player.name} played {card.formatCard()}")

def game(player, pile, list, x, i):
    
    playerTurnGreeting(player)
    while True:
        card = player.chooseFromHand()
        if checkLegal(card, pile):
            player.removeCard(card)

            playColorChange(card)
            playPlusCards(card, list[(x+1)%i], )
            playSkip(card)
            playSwitch(card)

            pile = card
            
            goodMove(player, card)
            break
        else:
            print("Please play a legal card or draw from the pile")
"""
decision = input('''Would you like to choose another card from your hand, or draw a card?
1. Chose from Hand
2. Draw''')

    if decision == "1":
        pass
    elif decision == "2" or decision == "":
        #Repeated draw mechanic
        
def draw

"""
        
        
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
    
