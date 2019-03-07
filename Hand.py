from Deck import *

class Hand:
    def __init__(self):
        self.cards = []
        self.highAces = 0
        self.score = 0
    def add_card(self, deck):
        self.cards.append(deck.deal_one())
        #check if it is an ace
        if self.cards[len(self.cards) - 1].value() == 11:
            self.highAces += 1
    def update_score(self):
        self.score = 0
        for i in self.cards:
            self.score += i.value()
        #if they busted out decrement high Aces and decrement value by 10
        if self.score > 21 and self.highAces > 0:
            self.highAces -= 1
            self.score -= 10