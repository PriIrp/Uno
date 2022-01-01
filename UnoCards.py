#Card class and constructor 
#Normal cards - 76 Numbered cards of 4 suits from 0-9
#Action cards - 8 2+ , 8 Skips, 8 Change
#Wild Cards - 4 4+ and 4 Color Change  
class Cards:
    suits = ["Red", "Yellow", "Blue", "Green"]
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

    def playPlusCards(self, player):    #Makes the next player draw a certain number of cards. Player parameter for Player Object. 
        if self.value == -2:            #Uses the draw method of the player class
            player.draw(2)
        elif self.suit == "4Plus":
            player.draw(4)
        
    def playColorChange(self):
        if self.suit == "Wild" or self.suit == "4Plus":
            c = int(input("""Choose the new color of the pile:
                                1. Red
                                2. Yellow
                                3. Blue
                                4. Green"""))
            self.value = suits[c-1]

 
            




    



    

    
