import random
from Card import *

class Deck:
    def __init__(self, numDecks, doshuffle):
        self.cards = []
        self.next = 0
        self.shuffle = doshuffle
        for i in range(numDecks):
            for s in ["Spades", "Hearts", "Diamonds", "Clubs"]:
                for r in range(2, 11):
                    self.cards.append(Card(str(r), s))
                for r in ["Jack", "Queen", "King", "Ace"]:
                    self.cards.append(Card(str(r), s))
        if self.shuffle:
            random.shuffle(self.cards)
    def reset(self):
        if self.shuffle:
            random.shuffle(self.cards)
        self.next = 0
    def deal_one(self):
        nextCard = self.cards[self.next]
        reset = False
        if(0 <= self.next < len(self.cards)):
            self.next += 1
        if(self.next == len(self.cards)):
            self.reset()
        return(nextCard)