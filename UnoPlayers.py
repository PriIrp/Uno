from UnoDeck import Deck


class Players(Deck):
    def __init__(self, name):
        self.name = name
        self.hand = []
        self.win = False
        self.cardNum = 0