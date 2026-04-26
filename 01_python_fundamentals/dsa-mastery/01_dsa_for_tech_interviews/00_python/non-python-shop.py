class Chai:
    def __init__ (self,sweetness,milk_level):
        self.sweetness = sweetness
        self.milk = milk_level
    
    def sip(self):
        print("Sipping the chai")

    def add_sugar(self,amount=""):
        print("Adding sugar")

my_Chai = Chai(sweetness="3",milk_level="high").sip()
Chai.add_sugar(my_Chai,2)