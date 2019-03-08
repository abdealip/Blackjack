class Card:
    def __init__(self, r, s):
        self.suit = s
        self.rank = r   #both strings
    def value(self):
        tenCards = ["Jack", "Queen", "King"]
        for i in tenCards:
            if self.rank == i:
                return(10)
        if self.rank == "Ace":
            return(11)
        if int(self.rank) in range(0, 11):
            return(int(self.rank))
    def __str__(self):
        return("The " + self.rank + " of " + self.suit)