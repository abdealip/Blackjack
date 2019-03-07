class Test:
    def __init__(self, int1, str1):
        self.num = int1
        self.name = str1
    def __str__(self):
        return(self.name + " " + str(self.num))