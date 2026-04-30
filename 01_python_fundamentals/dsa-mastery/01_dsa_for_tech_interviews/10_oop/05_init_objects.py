class ChaiOrder:
    def __init__(self,type_,size):
        self.type = type_
        self.size = size
    def summary(self):
        return f"{self.size}ml of {self.type}chai."

order = ChaiOrder("Masala",230)
print(order.summary())
order2 = ChaiOrder("Ginger",100)
print(order2.summary())
order3 = ChaiOrder("Black",240)
print(order3.summary())
order4 = ChaiOrder("Lemon",220)
print(order4.summary())

