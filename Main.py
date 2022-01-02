from UnoCards import Cards
from UnoDeck import Deck
import UnoPlayers as UP
from UnoGameLogic import game, checkWinner 


people = []
pile = Cards()

def initiateGame():
    global deck
    deck = Deck()
    deck.createDeck()
    deck.shuffle()

    UP.initPlayer(people)
    UP.initDraw(people, deck)

initiateGame()
print(people)
print(len(people))

x = 0
i = len(people)

while True:
    game(people[x%i], pile, people, deck)
    x += 1
    if checkWinner(people[x%i]):
        pass # Winner statement
        break