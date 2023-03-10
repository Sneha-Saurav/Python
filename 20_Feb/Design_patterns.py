# Factory Method 
#Burger Class

class CheeseBurger:
    def __init__(self):
        self.size = None

    def items(self):
        return "Cheese, Burger , Mayonnaise,Aloo tikki and Veggies"
    
    def price(self):
        if self.size == 'S':
            return 80.00
        if self.size == 'M':
            return 100.00
        if self.size == 'L':
            return 150.00
        
        
class VegBurger:
    def __init__(self):
        self.size = None

    def items(self):
        return "Cabbage ,Burger , Mayonnaise,Aloo tikki and Veggies and Sauce"
    
    def price(self):
        if self.size == 'S':
            return 70.00
        if self.size == 'M':
            return 120.00
        if self.size == 'L':
            return 170.00
        
        
class ChickenBurger:
    def __init__(self):
        self.size = None

    def items(self):
        return "Chicken tikka ,Burger , Mayonnaise,and Veggies and Sauce"
    
    def price(self):
        if self.size == 'S':
            return 100.00
        if self.size == 'M':
            return 150.00
        if self.size == 'L':
            return 200.00
        

       
class BeefBurger:
    def __init__(self):
        self.size = None

    def items(self):
        return "Beef, cooked patty, tikka ,Burger , Mayonnaise,and Veggies and Sauce"
    
    def price(self):
        if self.size == 'S':
            return 78.00
        if self.size == 'M':
            return 95.50
        if self.size == 'L':
            return 150.49
        
    
class FishBurger:
    def __init__(self):
        self.size = None

    def items(self):
        return "Fish tikki, tikka ,Burger , Mayonnaise,and Veggies and Sauce"
    
    def price(self):
        if self.size == 'S':
            return 108.00
        if self.size == 'M':
            return 159.50
        if self.size == 'L':
            return 120.49
        

class BurgerCombo:
    def __init__(self):
        self.size = None

    def items(self):
        return "French Fries , Coco Cola , Veg Burger with extra Cheese and toppings "
    
    def price(self):
        self.size = 'M'
        if self.size == "M":
            return 250.49
        
#Factory Function 
def BurgerFactory(burger):
    cls_dict = {
        'cheese':CheeseBurger(),
        'veg': VegBurger(),
        'chicken':ChickenBurger(),
        'beef': BeefBurger(),
        'fish':FishBurger(),
        'combo': BurgerCombo()
    }

    return cls_dict[burger.lower()]

# obj = BurgerFactory("cheese")
# # print(obj)
# # obj.size = "S"
# print(obj.price())

class_list =['cheese','veg','chicken','beef', 'fish', 'combo']
for x in class_list:
    obj = BurgerFactory(x)
    if x == 'combo':
        print("Items : {}".format(obj.items()))
        print("Price: {}".format(obj.price()))
        print("__________________________________________________________________________")

    else:
        print("Items : {}".format(BurgerFactory(x).items()))
        obj.size="S"
        print("Price for S size : {}".format(obj.price()))
        obj.size="M"
        print("Price for M size : {}".format(obj.price()))
        obj.size="L"
        print("Price for L size : {}".format(obj.price()))
        print("__________________________________________________________________________")







        


         


