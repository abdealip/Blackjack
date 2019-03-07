import random

class Player:
    def __init__(self, player):
        self.hand = Hand()
        #is_dealer is a bool
        self.money = is_dealer*100
    def deal_hand(self, deck):
        self.hand.add_card(deck)
        self.hand.add_card(deck)

    def add_card(self, deck):
        self.hand.add_card(deck)
    def bust(self):
        pass

class NonDealer(Player):
    def get_input(self):
        pass


def blackjack():
    deck = []
    for i in ["Spades", "Hearts", "Clubs", "Diamonds"]:
        for j in range(2,11):
            deck.append("The "+str(j)+" of "+str(i))
        for k in ["Jack","Queen","King","Ace"]:
            deck.append("The "+str(k)+" of "+str(i))
    ranks = []
    for i in range(2,11):
        ranks.append(str(i))
    for i in ["Jack", "Queen", "King", "Ace"]:
        ranks.append(i)
    cardValues = {}
    for i in deck:
        for j in range(2,11):
            if str(j) in i:
                cardValues[i] = j
        for k in ["Jack", "Queen", "King"]:
            if k in i:
                cardValues[i] = 10
        if "Ace" in i:
            cardValues[i] = 11
    dealer = []
    player = []
    playerMoney = 100
    end = False
    print("Rules:")
    print("The dealer plays his hand first, until he stands or busts.")
    print("You will only see one of the dealer's cards.")
    print("After the dealer stands, you will play your hand until you stand or bust.")
    print("If you both bust, the dealer wins.")
    print("Blackjacks win if you both get 21")
    print("If there are no blackjacks and the score is tied, it is a tie.")
    print("You get $100 to start with. The game pays 3-2.")
    consent = input("If you are ready to start, hit enter.")
    print("--------------------------------------------------------------------------")
    while end == False:
        try:
            for i in range(2):
                x = random.choice(deck)
                deck.remove(x)
                dealer.append(x)
                y = random.choice(deck)
                deck.remove(y)
                player.append(y)
            reveal = random.choice(dealer)
            print("Dealer's faceup card: " + str(reveal))
            dealerScore = 0
            for i in dealer:
                dealerScore += cardValues[i]
            if dealerScore > 21:
                cardValues[dealer[0]] = 1
                dealerCardScores = []
                for i in dealer:
                    dealerCardScores.append(cardValues[i])
                dealerScore = sum(dealerCardScores)
            while dealerScore < 17:         #DealerLoop
                x = random.choice(deck)
                deck.remove(x)
                dealer.append(x)
                dealerScore += cardValues[x]
                dealerHighAces = []         #Dealer stays on soft seventeens
                if dealerScore > 21:
                    try:
                        for i in dealer:
                            if cardValues[i] == 11:          #Selects a High Ace, if it exists
                                dealerHighAces.append(i)
                        x = random.choice(dealerHighAces)
                        cardValues[x] = 1       #Turns a High Ace into A Low Ace
                        dealerHighAces.remove(x)    #Just in case the dealer gets all four aces
                        dealerCardScores = []
                        for i in dealer:
                            dealerCardScores.append(cardValues[i])
                        dealerScore = sum(dealerCardScores)
                    except:     #Dealer Actually Busts
                        pass
            bet = int(input("How much would you like to bet?\nType a number, then hit enter:"))
            print("Your hand:")     #
            for i in player:        #
                print(i)            #Showing the player his hand
            playerScore = 0
            for i in player:
                playerScore += cardValues[i]
            if playerScore > 21:
                cardValues[player[0]] = 1
                playerCardScores = []
                for i in player:
                    playerCardScores.append(cardValues[i])
                playerScore = sum(playerCardScores)
            satisfaction = False
            split = False
            for i in ranks:
                if i in player[0] and i in player[1]:
                    print("Would you like to split?")
                    split = input("Type y for yes or n for no")
                    if split == "y":
                        split = True
                    elif split == "n":
                        split = False
            if split == True:
                playerScore = 0
                hand1 = []
                hand2 = []
                hand1.append(player[0])
                hand2.append(player[1])
                player = []             #That's all the list stuff out of the way
                bet1 = bet              #The original bet is on hand1
                bet2 = int(input("How much would you like to bet on your second hand?\nType a number, then hit enter:"))
                #This marks the start of play for hand1
                x = random.choice(deck)
                deck.remove(x)
                hand1.append(x)
                print("You have bet $" + str(bet1) + " on your first hand, which consists of:")
                for i in hand1:
                    print(i)
                #First, we check for double aces in hand1
                handScore1 = 0
                for i in hand1:
                    handScore1 += cardValues[i]
                if handScore1 > 21:
                    cardValues[hand1[0]] = 1
                    handCardScores1 = []
                    for i in hand1:
                        handCardScores1.append(cardValues[i])
                    handScore1 = sum(handCardScores1)
                satisfaction = False
                #Hitloop for hand1
                while handScore1 <= 21 and satisfaction == False:                    #PlayerLoop
                    decision = input("Type h to hit or s to stand, then hit Enter: ")
                    if decision == "s":
                        satisfaction = True
                        continue            #continue means screw the rest of the loop and move on
                    elif decision == "h":
                        x = random.choice(deck)
                        deck.remove(x)
                        hand1.append(x)
                        handScore1 += cardValues[x]
                        print("You have received " + str(x))
                    handHighAces1 = []
                    if handScore1 > 21:
                        try:
                            for i in hand1:
                                if cardValues[i] == 11:          #Selects a High Ace, if it exists
                                    handHighAces1.append(i)
                            x = random.choice(handHighAces1)
                            cardValues[x] = 1       #Turns a High Ace into A Low Ace
                            handHighAces1.remove(x)    #Just in case the player gets all four aces
                            handCardScores1 = []
                            for i in player:
                                handCardScores1.append(cardValues[i])
                            handScore1 = sum(handCardScores1)
                        except:
                            pass
                #This marks the start of play for hand2
                print("--------------------------------------------------------------------------")
                x = random.choice(deck)
                deck.remove(x)
                hand2.append(x)
                print("You have bet $" + str(bet2) + " on your second hand, which consists of:")
                for i in hand2:
                    print(i)
                #First, we check for double aces in hand2
                handScore2 = 0
                for i in hand2:
                    handScore2 += cardValues[i]
                if handScore2 > 21:
                    cardValues[hand2[0]] = 1
                    handCardScores2 = []
                    for i in hand2:
                        handCardScores2.append(cardValues[i])
                    handScore2 = sum(handCardScores2)
                satisfaction = False
                #Hitloop for hand2
                while handScore2 <= 21 and satisfaction == False:                    #PlayerLoop
                    decision = input("Type h to hit or s to stand, then hit Enter: ")
                    if decision == "s":
                        satisfaction = True
                        continue            #continue means screw the rest of the loop and move on
                    elif decision == "h":
                        x = random.choice(deck)
                        deck.remove(x)
                        hand2.append(x)
                        handScore2 += cardValues[x]
                        print("You have received " + str(x))
                    handHighAces2 = []
                    if handScore2 > 21:
                        try:
                            for i in hand2:
                                if cardValues[i] == 11:         #Selects a High Ace, if it exists
                                    handHighAces2.append(i)
                            x = random.choice(handHighAces2)
                            cardValues[x] = 1       #Turns a High Ace into A Low Ace
                            handHighAces2.remove(x)    #Just in case the player gets all four aces
                            handCardScores2 = []
                            for i in player:
                                handCardScores2.append(cardValues[i])
                            handScore2 = sum(handCardScores2)
                        except:
                            pass
            else:                                               #This is if the player doesn't split
                while playerScore <= 21 and satisfaction == False:                    #PlayerLoop
                    decision = input("Type h to hit or s to stand, then hit Enter: ")
                    if decision == "s":
                        satisfaction = True
                    elif decision == "h":
                        x = random.choice(deck)
                        deck.remove(x)
                        player.append(x)
                        playerScore += cardValues[x]
                        print("You have received " + str(x))
                    playerHighAces = []
                    if playerScore > 21:
                        try:
                            for i in player:
                                if cardValues[i] == 11:          #Selects a High Ace, if it exists
                                    playerHighAces.append(i)
                            x = random.choice(playerHighAces)
                            cardValues[x] = 1       #Turns a High Ace into A Low Ace
                            playerHighAces.remove(x)    #Just in case the player gets all four aces
                            playerCardScores = []
                            for i in player:
                                playerCardScores.append(cardValues[i])
                            playerScore = sum(playerCardScores)
                        except:
                            pass
            #At this point the dealer and the player are satisfied or have busted out
            print("--------------------------------------------------------------------------")
            print("The Dealer's Hand:")
            for i in dealer:
                print(i)
            if dealerScore <= 21:
                print("The Dealer's Score: " + str(dealerScore))
            else:
                print("The dealer busted out!")
            #Final Results
            if split == True:                               #If this doesn't work try if playerScore == 0
                print("Here is what happened on your first hand:")
                print("Your First Hand:")
                for i in hand1:
                    print(i)
                if handScore1 <= 21:
                    print("Your First Hand's Score: " + str(handScore1))
                else:
                    print("You busted out!")
                if handScore1 > 21 and dealerScore > 21:
                    print("You both busted! Dealer wins!")
                    print("Your bet: $" + str(bet1))
                    playerMoney -= bet1
                elif handScore1 > 21 and dealerScore <= 21:
                    print("You busted! Dealer wins!")
                    print("Your bet: $" + str(bet1))
                    playerMoney -= bet1
                elif handScore1 <= 21 and dealerScore > 21:
                    print("The dealer busted! You win!")
                    print("Your bet: $" + str(bet1))
                    playerMoney += bet1*1.5
                elif handScore1 <= 21 and dealerScore <= 21:
                    if handScore1 < dealerScore:
                        print("Dealer wins!")
                        print("Your bet: $" + str(bet1))
                        playerMoney -= bet1
                    elif handScore1 > dealerScore:
                        print("You win!")
                        print("Your bet: $" + str(bet1))
                        playerMoney += bet1*1.5
                    elif handScore1 == dealerScore:
                        if handScore1 == 21:
                            if len(hand1) == 2 and len(dealer) == 2:
                                print("You both got blackjacks! It's a tie!")
                            elif len(hand1) == 2 and len(dealer) != 2:
                                print("You got a blackjack! You win!")
                                print("Your bet: $" + str(bet1))
                                playerMoney += bet1*1.5
                            elif len(hand1) != 2 and len(dealer) == 2:
                                print("The dealer got a blackjack! Dealer wins!")
                                print("Your bet: $" + str(bet1))
                                playerMoney += bet1*1.5
                            elif len(hand1) != 2 and len(dealer) != 2:
                                print("Neither of you got a blackjack! It's a tie!")
                        else:
                            print("You both got the same score! It's a tie!")
                print("--------------------------------------------------------------------------")
                #Second hand results
                print("Here is what happened on your second hand:")
                print("Your Second Hand:")
                for i in hand2:
                    print(i)
                if handScore2 <= 21:
                    print("Your Second Hand's Score: " + str(handScore2))
                else:
                    print("You busted out!")
                if handScore2 > 21 and dealerScore > 21:
                    print("You both busted! Dealer wins!")
                    print("Your bet: $" + str(bet2))
                    playerMoney -= bet2
                elif handScore2 > 21 and dealerScore <= 21:
                    print("You busted! Dealer wins!")
                    print("Your bet: $" + str(bet2))
                    playerMoney -= bet2
                elif handScore2 <= 21 and dealerScore > 21:
                    print("The dealer busted! You win!")
                    print("Your bet: $" + str(bet2))
                    playerMoney += bet2*1.5
                elif handScore2 <= 21 and dealerScore <= 21:
                    if handScore2 < dealerScore:
                        print("Dealer wins!")
                        print("Your bet: $" + str(bet2))
                        playerMoney -= bet2
                    elif handScore2 > dealerScore:
                        print("You win!")
                        print("Your bet: $" + str(bet1))
                        playerMoney += bet2*1.5
                    elif handScore2 == dealerScore:
                        if handScore2 == 21:
                            if len(hand2) == 2 and len(dealer) == 2:
                                print("You both got blackjacks! It's a tie!")
                            elif len(hand2) == 2 and len(dealer) != 2:
                                print("You got a blackjack! You win!")
                                print("Your bet: $" + str(bet2))
                                playerMoney += bet2*1.5
                            elif len(hand2) != 2 and len(dealer) == 2:
                                print("The dealer got a blackjack! Dealer wins!")
                                print("Your bet: $" + str(bet1))
                                playerMoney += bet2*1.5
                            elif len(hand2) != 2 and len(dealer) != 2:
                                print("Neither of you got a blackjack! It's a tie!")
                        else:
                            print("You both got the same score! It's a tie!")
            else:                                           #If the player didn't split
                print("Your Hand:")
                for i in player:
                    print(i)
                if playerScore <= 21:
                    print("Your Score: " + str(playerScore))
                else:
                    print("You busted out!")
                if playerScore > 21 and dealerScore > 21:
                    print("You both busted! Dealer wins!")
                    print("Your bet: $" + str(bet))
                    playerMoney -= bet
                elif playerScore > 21 and dealerScore <= 21:
                    print("You busted! Dealer wins!")
                    print("Your bet: $" + str(bet))
                    playerMoney -= bet
                elif playerScore <= 21 and dealerScore > 21:
                    print("The dealer busted! You win!")
                    print("Your bet: $" + str(bet))
                    playerMoney += bet*1.5
                elif playerScore <= 21 and dealerScore <= 21:
                    if playerScore < dealerScore:
                        print("Dealer wins!")
                        print("Your bet: $" + str(bet))
                        playerMoney -= bet
                    elif playerScore > dealerScore:
                        print("You win!")
                        print("Your bet: $" + str(bet))
                        playerMoney += bet*1.5
                    elif playerScore == dealerScore:
                        if playerScore == 21:
                            if len(player) == 2 and len(dealer) == 2:
                                print("You both got blackjacks! It's a tie!")
                            elif len(player) == 2 and len(dealer) != 2:
                                print("You got a blackjack! You win!")
                                print("Your bet: $" + str(bet))
                                playerMoney += bet*1.5
                            elif len(player) != 2 and len(dealer) == 2:
                                print("The dealer got a blackjack! Dealer wins!")
                                print("Your bet: $" + str(bet))
                                playerMoney += bet*1.5
                            elif len(player) != 2 and len(dealer) != 2:
                                print("Neither of you got a blackjack! It's a tie!")
                        else:
                            print("You both got the same score! It's a tie!")
            print("Your money: $" + str(playerMoney))
            print("Do you want to play another round?")
            newConsent = input("Type y for Yes or n for No, then hit enter.")
            if newConsent == "y":
                end = False
                player = []
                dealer = []
                playerScore = 0
                dealerScore = 0
                try:
                    del hand1
                    del hand2
                    del handScore1
                    del handScore2
                    del handCardScores1
                    del handCardScores2
                    del handHighAces1
                    del handHighAces2
                except:
                    pass
                print("--------------------------------------------------------------------------")
            elif newConsent == "n":
                end = True
        except:
            print("The deck ran out. Let's get a new one shall we?")
            deck = []
            for i in ["Spades", "Hearts", "Clubs", "Diamonds"]:
                for j in range(2,11):
                    deck.append("The "+str(j)+" of "+str(i))
                for k in ["Jack","Queen","King","Ace"]:
                    deck.append("The "+str(k)+" of "+str(i))
            user = input("Press Enter to Continue")
            print("--------------------------------------------------------------------------")
#blackjack()
