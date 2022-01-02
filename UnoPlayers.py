class Players():
    def __init__(self, name):
        self.name = name
        self.hand = []
        self.win = False
        self.cardNum = 0

    def draw(self, deck):
        self.hand.append(deck.draw())
        self.cardNum += 1

    def removeCard(self, card):
        self.hand.remove(card)
        self.cardNum -=1

    def showHand(self):
        display = []
        for i in range(0, len(self.hand)-1):
            display.append(self.hand[i].formatCard())
        print(display)

    def chooseFromHand(self):
        for i in range(0, len(self.hand)-1):
            print(f"{i}: {self.hand[i].formatCard()}")
        chosen = int(input("Choose what card to play: "))
        return self.hand[chosen]
    
    

    def isWinner(self):
        if self.cardNum == 0:
            self.win = True
            return True
    

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
            