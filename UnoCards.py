#Card class and constructor 
suits = ["Red", "Yellow", "Blue", "Green"]

class Cards:
    def __init__(self, suit, value=None):
        self.suit = suit
        self.value = value

    def playWild(self):
        if self.suit == "Wild":
            c = int(input("""Choose the new color of the pile:
                                1. Red
                                2. Yellow
                                3. Blue
                                4. Green"""))
            self.value = suits[c-1]

    def checkLegal(self, obj):
        if self.value == obj.value:
            return True
        elif self.suit == obj.value:
            return True
        else:
            return False
            

#Loop for creating cards
#Normal cards - 76 Numbered cards of 4 suits from 0-9
#Action cards - 8 2+ , 8 Skips, 8 Change
#Wild Cards - 4 4+ and 4 Color Change           
def createDeck():
    for i in suits:
        for r in range(0,10):  #Num cards
            Cards(i,r)


        for r in range(0,3):    #Action cards
            for j in range(0,2):
                Cards(i, -1-r)

        Cards(i,-4)             #4+ cards

        Cards("Wild")             #Wild


    



    

    
