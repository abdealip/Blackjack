from Deck import *

class Hand:
    def __init__(self):
        self.cards = []
        self.highAces = 0
        self.score = 0
        self.bet = 0
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
    def size(self):
        return(len(self.cards))
    def splittable(self):
        if self.size() != 2:
            return False
        return(self.cards[0] == self.cards[1])
    def split(self):
        #return the second hand and modify current hand
        hand2 = Hand()
        hand2.cards.append(self.cards[1])
        self.cards.pop()
        return(hand2)
    def __str__(self):
        answer = ""
        for i in range(len(self.cards)):
            answer += str(self.cards[i])
            if i != len(self.cards) - 1:
                answer += "\n"
        return(answer)
    def bust(self):
        self.update_score()
        if self.score > 21:
            return(True)
        return(False)