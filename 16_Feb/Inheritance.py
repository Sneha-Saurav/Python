# Types of Inheritance


#1. Single  Inheritance 
class Brands:
   def __init__(self, name):
      self.name = name
    
   
class Products(Brands):
    def __init__(self,name,item):
      Brands.__init__(self,name)
      self.item = item
    def __str__(self):    # dunder method 
       return "Brand: {} , Product: {}".format(self.name, self.item)

print("###############################################################################")      
p1 = Products("Apple", 'Mobile  Phone')
print(p1)


class Parent:
   def info(self):
      return "I am a parent."
   
class Child(Parent):
   def child_info(self):
      return "I am child of the Parent"

c1 = Child()
print(c1.info())
print(c1.child_info())

print("###############################################################################")      



# Multiple Inheritance 
class Brands:
    def __init__(self,name):
      self.name = name
    
    def __repr__(self):
       return "Brand Name: {} ".format(self.name)
#Ex 1
class Products:
   def __init__(self,item_name):
      self.item_name = item_name

   def __repr__(self):
      return "Product Name:{} ".format(self.item_name)  
   
class Stock(Brands, Products):
    def __init__(self, no_of_stocks):
        self.no_of_stocks = no_of_stocks

    def __repr__(self):
       return "Available : {}".format(self.no_of_stocks)
    

b1 = Brands("JBL")
p1 = Products("Earphones")
s1 = Stock(100)
print(b1)
print(p1)
print(s1)   

#Ex 2
class Profit:
   def __init__(self, profit):
      self.profit = profit
    
   def profit_show(self):
      return "Profit: {} ".format(self.profit)

class Loss:
    def __init__(self, loss):
      self.loss = loss

    def loss_show(self):
      return "Loss : {} ".format(self.loss)
    
class Balance(Profit, Loss):
   def __init__(self, amount):
      self.amount = amount

   def show_balance(self):
      return"Balance is : {} ".format(self.amount)
   

p1 = Profit(1200)
l1 = Loss(120)
b1 = Balance(12500)
print(p1.profit_show() + l1.loss_show() + b1.show_balance())

print("###############################################################################") 


# Multilevel Inheritance 
class Person:
    def __init__(self,name):
      self.name = name
    
    def show(self):
       return "Name :{} ".format(self.name)
    
class Employee(Person):
    def __init__(self, name , position):
      super().__init__(name)
      self.position  = position

    def __str__(self):
       return self.position

class Developer(Employee):
    def __init__(self,name, position, programming_language):
      super().__init__(name, position)
      self.programming_language = programming_language

    def __str__(self):
       return self.programming_language
    

user = Developer("Sneha Saurav", 'Intern','Python')
print(user.show())
print("Position:{}".format(user.position)) 
print("Technology: {}".format(user))
      
   
      
   

# Python program to demonstrate
# multilevel inheritance
 
# Base class
 
 
class Grandfather:
 
    def __init__(self, grandfather):
        self.grandfather = grandfather
 
class Father(Grandfather):
    def __init__(self, fathername, grandfather):
        self.fathername = fathername
 
       
        Grandfather.__init__(self, grandfather)
 
class Son(Father):
    def __init__(self, sonname, fathername, grandfather):
        self.sonname = sonname
 
        Father.__init__(self, fathername, grandfather)
 
    def print_name(self):
        print('Grandfather name :', self.grandfather)
        print("Father name :", self.fathername)
        print("Son name :", self.sonname)


s1 =Son("Ishwar Pal", 'Ashish Kumar','Rajat')
s1.print_name()


    
       