#Card class and constructor 
#Normal cards - 76 Numbered cards of 4 suits from 0-9
#Action cards - 8 2+ , 8 Skips, 8 Change
#Wild Cards - 4 4+ and 4 Color Change  
suits = ["Red", "Yellow", "Blue", "Green"]
class Cards:
    def __init__(self, suit=None, value=None):
        self.suit = suit
        self.value = value

    def formatCard(self):
        if self.value is not None:
            if self.value >= 0:
                return f"{self.suit} {self.value}"
            elif self.value == -1:
                return f"{self.suit} 2+"
            elif self.value == -2:
                return f"{self.suit} Skip Turn"
            elif self.value == -3:
                return f"{self.suit} Reverse"
        elif self.value is None:
            if self.suit == "4PLus":
                return "Draw 4"
            elif self.suit == "Wild":
                return "Wild"

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
 
            




    



    

    
