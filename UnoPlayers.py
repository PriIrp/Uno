from UnoDeck import Deck

playerList = []
class Players(Deck):
    def __init__(self, name):
        super().__init__()
        self.name = name
        self.hand = []
        self.win = False
        self.cardNum = 0

    def draw(self, deck):
        self.hand.append(deck.draw())

def initPlayer(list):
    global raw_name
    raw_name = input("""Enter the names of all the players who will play Uno. Seperate by a comma (,)
    
            Enter names: """)

    raw_name_list = raw_name.split(",")
    for n in raw_name_list:
        list.append(Players(n))

def initDraw(list):                         #Has every player draw 7 cards
    for i in range(0,7):
        for p in range(0, len(raw_name)):
            list[p].draw()


# initPlayer(playerList)
# initDraw(playerList)

P1 = Players("Pri")
d = Deck()
d.createDeck()
P1.draw(d)
P1.draw(d)
print(P1.hand)
