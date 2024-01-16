class Burger:
    def __init__(self, ingredients: list) -> None:
        self.ingredients = ingredients
    
    def print(self):
        print(self.ingredients)

class BurgerFactory:
    def createCheeseburger(self) -> Burger:
        ingredients = ["bun", "cheese", "patty"]
        return Burger(ingredients)
    def deluxeBurger(self) -> Burger:
        ingredients = ["bun", "cheese", "bacon", "patty"]
        

cheese = BurgerFactory().createCheeseburger()
deluxe = BurgerFactory().deluxeBurger()