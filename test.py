from Card import *
from Hand import *
from Players import *

deck = Deck(1, False)
x = Hand()
x.cards.append(Card("Ace", "Spades"))
x.cards.append(Card("Ace", "Hearts"))

p = NonDealer(False)
p.hand = x
p.hands = [x]
print("Your hand:\n" + str(x))

print("Would you like to split?")
splitInput = input("Type y for yes or n for no: ")
if splitInput == "y":
    split = True
elif splitInput == "n":
    split = False
if split:
    p.hands.append(p.hand.split())
print(p.hands[0])
print()
print(p.hands[1])