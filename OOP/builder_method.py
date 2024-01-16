class Burger:
    def __init__(self) -> None:
        self.buns = None
        self.patty = None
        self.cheese = None
    
    def setBuns(self, bunStyle):
        self.buns = bunStyle
    
    def setPatty(self, pattyStyle):
        self.patty = pattyStyle
    def setCheese(self, cheeseStyle):
        self.cheese = cheeseStyle
        
class BurgerBuilder:
    def __init__(self) -> None:
        self.burger = Burger()
    
    def addBuns(self, buns):
        self.burger.setBuns(buns)
        return self
    def addPatty(self, patty):
        self.burger.setPatty(patty)
        return self
    def addCheese(self, cheese):
        self.burger.setCheese(cheese)
        return self
    def build(self):
        return self.burger
    

burg = BurgerBuilder().addBuns("sesame").addPatty("meat").addCheese("swiss").build()