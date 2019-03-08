from Deck import *
from Hand import *

class Player:
    def __init__(self, is_dealer):
        self.hand = Hand()
        self.hands = [self.hand]
        #is_dealer is a bool
        self.money = is_dealer*100
    def deal_hand(self, deck):
        self.hand.add_card(deck)
        self.hand.add_card(deck)

class NonDealer(Player):
    def requestBet(self):
        print("How much would you like to bet?")
        bet = int(input("Type a number, then hit enter: "))
        return(bet)
    def split(self):
        #splitting
        if self.hand.splittable():
            print("Would you like to split?")
            splitInput = input("Type y for yes or n for no")
            if splitInput == "y":
                split = True
            elif splitInput == "n":
                split = False
        if split:
            self.hands.append(self.hands[0].split())
    def hitLoop(self, deck):
        satisfaction = False
        #insert for loop for array of hands
        for i in range(len(hands)):
            while not hands[i].bust() and satisfaction == False:
                print("Your hand\n" + str(hands[i]))
                decision = input("Type h to hit or s to stand, then hit Enter: ")
                if decision == "s":
                    satisfaction = True
                elif decision == "h":
                    hand.add_card(deck)
    def playHand(self, deck):
        for i in range(len(hands)):
            hands[i].bet = self.requestBet()
        self.split()
        self.hitLoop(deck)