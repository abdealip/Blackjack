import random
from Players import *

class Game:
    def __init__(self, numPlayers, numDecks, shuffle):
        self.dealer = Dealer(True)
        self.players = []
        for i in range(numPlayers):
            p = NonDealer(False)
            self.players.append(p)
        self.deck = Deck(numDecks, shuffle)
    def setNames(self):
        for i in range(len(self.players)):
            self.players[i].requestName(i+1)
    def placeBets(self):
        for i in self.players:
            i.requestBet(0)
    def playRound(self):
        self.dealer.deal(self.deck)
        self.placeBets()
        for i in range(len(self.players)):
            self.players[i].deal_hand(self.deck)
        for i in range(len(self.players)):
            print(self.players[i].name + ":")
            self.players[i].playHand(self.deck)
            printLine()
        self.dealer.playHand(self.deck)
    def showResults(self):
        print("Dealer's hand:")
        print(self.dealer.hand)
        printLine()
        if self.dealer.hand.bust():
            for p in range(len(self.players)):
                for h in range(len(self.players[p].hands)):
                    print(self.players[p].name + ":")
                    print(self.players[p].hands[h])
                    if not self.players[p].hands[h].bust():
                        self.players[p].updateMoney(True, h)
                    else:
                        self.players[p].updateMoney(False, h)
                print(self.players[p].name + ", you have $" + str(self.players[p].money))
        else:
            for p in range(len(self.players)):
                for h in range(len(self.players[p].hands)):
                    print(self.players[p].name + ":")
                    print(self.players[p].hands[h])
                    if self.players[p].hands[h].bust():     #if the player busts they lose regardless
                        self.players[p].updateMoney(False, h)
                    elif self.players[p].hands[h].score > self.dealer.hand.score:
                        self.players[p].updateMoney(True, h)
                    elif self.players[p].hands[h].score == self.dealer.hand.score:
                        if self.players[p].hands[h].is_blackjack():
                            if not self.dealer.hand.is_blackjack():
                                self.players[p].updateMoney(True, h)
                            else:
                                pass    #both player and dealer have blackjacks
                        else:
                            if self.dealer.hand.is_blackjack():
                                self.players[p].updateMoney(False, h)   #dealer has blackjack, player does not
                            else:
                                pass    #both player and dealer do not have blackjacks
                    else:
                        self.players[p].updateMoney(False, h)
                print(self.players[p].name + ", you have $" + str(self.players[p].money))
    def reset(self):
        for p in range(len(self.players)):
            self.players[p].reset()
        self.dealer.reset()

def printLine():
    print("--------------------------------------------------------------------------")

def showRules():
    print("Rules:")
    print("You will only see one of the dealer's cards.")
    print("After all players are done playing their hands, the dealer will play his hand.")
    print("The dealer will continue to hit until he reaches a soft (or hard) 17")
    print("If you both bust, the dealer wins.")
    print("Blackjacks win if you both get 21")
    print("If there are no blackjacks and the score is tied, it is a tie.")
    print("You get $100 to start with. The game pays 3-2.")
    consent = input("If you are ready to start, hit enter.")

def blackjack():
    numPlayers = int(input("How many players? "))
    numDecks = int(input("How many decks? "))
    shuffle = bool(int(input("Shuffle? 1 for yes, 0 for no: ")))
    print(shuffle)
    showRules()
    printLine()
    g = Game(numPlayers, numDecks, shuffle)
    g.setNames()
    printLine()
    done = False
    while not done:
        consented = False
        g.playRound()
        g.showResults()
        printLine()
        print("Do you want to play another round?")
        while not consented:
            newConsent = input("Type y for Yes or n for No, then hit enter: ")
            if newConsent == "n":
                done = True
                consented = True
            elif newConsent == "y":
                consented = True
        g.reset()
        printLine()

blackjack()
