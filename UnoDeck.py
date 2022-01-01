from UnoCards import Cards
import random

class Deck:
    def __init__(self):
        self.deck = []
        self.suits = ["Red", "Yellow", "Blue", "Green"]
    
    def createDeck(self):
        for i in self.suits:
            for r in range(0,10):               #Num cards
                self.deck.append(Cards(i,r))


            for r in range(0,3):                #Action cards
                for j in range(0,2):                #-2 for 2+ | -3 for Skip | -4 for Direction
                    self.deck.append(Cards(i, -1-r)) 
        
            self.deck.append(Cards("4Plus"))                    #4+ cards

            self.deck.append(Cards("Wild"))                     #Wild

    def shuffle(self):
        random.shuffle(self.deck)

    def draw(self):
        card = self.deck.pop(0)
        return card