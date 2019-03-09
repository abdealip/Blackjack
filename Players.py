from Hand import *

class Player:
    def __init__(self, is_dealer):
        self.hand = Hand()
        self.hands = [self.hand]
        #is_dealer is a bool
        self.money = (1-is_dealer)*100
        self.name = ""
    def deal_hand(self, deck):
        self.hand.add_card(deck)
        self.hand.add_card(deck)
    def reset(self):
        self.hand = Hand()
        self.hands = [self.hand]

class Dealer(Player):
    def deal(self, deck):
        self.deal_hand(deck)
        print("Dealer's faceup card: " + str(self.hand.cards[0]))
    def playHand(self, deck):
        while not self.hand.bust() and self.hand.score < 17:
            self.hand.add_card(deck)

class NonDealer(Player):
    def requestName(self, n):
        self.name = input("Player " + str(n) + ", please enter your name: ")
    def requestBet(self, hand):
        if hand == 0:
            print(self.name + ", how much would you like to bet?")
        elif hand == 1:
            print(self.name + ", how much would you like to bet on your second hand?")
        self.hands[hand].bet = int(input("Type a number, then hit enter: "))
    def split(self):
        #splitting
        split = False
        if self.hand.splittable() and len(self.hands) == 1:
            print("Your hand:")
            print(self.hands[0])
            print("Would you like to split?")
            splitInput = input("Type y for yes or n for no: ")
            if splitInput == "y":
                split = True
            elif splitInput == "n":
                split = False
        if split:
            self.hands.append(self.hands[0].split())
    def hitLoop(self, deck):
        for i in range(len(self.hands)):
            satisfaction = False
            while not self.hands[i].bust() and not satisfaction:
                print("Your hand\n" + str(self.hands[i]))
                if self.hands[i].double_down():
                    self.hands[i].add_card(deck)
                    self.hands[i].bet*= 2
                    print(self.hands[i])
                    satisfaction = True
                    break
                decision = input("Type h to hit or s to stand, then hit Enter: ")
                if decision == "s":
                    satisfaction = True
                elif decision == "h":
                    self.hands[i].add_card(deck)
            if self.hands[i].bust():
                print("Your hand:")
                print(self.hands[i])
                print("You busted out!")
    def playHand(self, deck):
        self.split()
        if len(self.hands) == 2:
            self.requestBet(1)
        self.hitLoop(deck)
    def updateMoney(self, won, handIndex):
        if won:
            if len(self.hands) == 2 and self.hands[handIndex].is_blackjack():
                self.money += self.hands[handIndex].bet
            else:
                self.money += self.hands[handIndex].bet*1.5
        else:
            self.money -= self.hands[handIndex].bet