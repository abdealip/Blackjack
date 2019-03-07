class Abstract:
    def __init__(self, int1, int2, int3):
        self.num1 = int1
        self.num2 = int2
        self.num3 = int3
    def total(self):
        return(self.num1 + self.num2 + self.num3)

class Derived(Abstract):
    def product(self):
        return(self.num1*self.num2*self.num3)
    def total(self):
        return(self.num1 + self.num2)

a = Derived(2, 4, 3)
b = Abstract(1, 4, 9)
print(b.total())
print(a.total())
print(a.product())