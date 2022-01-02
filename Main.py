from UnoCards import Cards
from UnoDeck import Deck
import UnoPlayers as UP
from UnoGameLogic import game, checkWinner 

suits = ["Red", "Yellow", "Blue", "Green"]
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

x = 0 
i = len(people)-1

while True:
    game(people[x%i], pile, people, x, i)
    x += 1
    if checkWinner(people[x%i]):
        pass # Winner statement
        break