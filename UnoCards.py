#Card class and constructor 
#Normal cards - 76 Numbered cards of 4 suits from 0-9
#Action cards - 8 2+ , 8 Skips, 8 Change
#Wild Cards - 4 4+ and 4 Color Change  

suits = ["Red", "Yellow", "Blue", "Green"]

class Cards:
    def __init__(self, suit, value=None):
        self.suit = suit
        self.value = value

    def checkLegal(self, obj):
        if self.value == obj.value:
            return True
        elif self.suit == obj.value:
            return True
        elif self.suit == "Wild" or self.suit == "4Plus":
            return True
        else:
            print("Please play a legal move")
            return False

    def playPlusCards(self, player):
        if self.value == -2 or self.suit == "4Plus":
            player.draw()
        

    def playColorChange(self):
        if self.suit == "Wild" or self.suit == "4Plus":
            c = int(input("""Choose the new color of the pile:
                                1. Red
                                2. Yellow
                                3. Blue
                                4. Green"""))
            self.value = suits[c-1]

 
            

#Loop for creating cards
def createDeck():
    for i in suits:
        for r in range(0,10):               #Num cards
            Cards(i,r)


        for r in range(0,3):                #Action cards
            for j in range(0,2):                #-2 for 2+ | -3 for Skip | -4 for Direction
                Cards(i, -1-r)  
    
        Cards("4Plus")                      #4+ cards

        Cards("Wild")                       #Wild


    



    

    
