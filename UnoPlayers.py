from UnoDeck import Deck
from UnoCards import Cards

playerList = []
class Players():
    def __init__(self, name):
        self.name = name
        self.hand = []
        self.win = False
        self.cardNum = 0

    def draw(self, deck):
        self.hand.append(deck.draw())

    def showHand(self):
        for i in range(0, len(self.hand)-1):
            self.hand[i].showCard()

        

def initPlayer(list):
    global raw_name
    raw_name = input("""Enter the names of all the players who will play Uno. Seperate by a comma (,)
    
            Enter names: """)

    raw_name_list = raw_name.split(",")
    for n in raw_name_list:
        list.append(Players(n))

def initDraw(list, deck):                         #Has every player draw 7 cards
    for i in range(0,7):
        for p in range(0, len(list)-1):
            list[p].draw(deck)


# initPlayer(playerList)
# initDraw(playerList)

d = Deck()
d.createDeck()
d.shuffle()

initPlayer(playerList)
initDraw(playerList, d)

print(len(playerList))
print(len(playerList[0].hand))

print(type(playerList[0].hand[0]))
playerList[0].showHand()