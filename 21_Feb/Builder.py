
class Person:
    def __init__(self):
        self.name = None
        self.degree = None
        self.car= None
        self.house = None
    
    def Name(self, name):
        self.name = name
        return self.name
    
    def Degree(self, deg):
        self.degree = deg
        return self.degree

    def Car(self, car):
        self.car = car
        return self.car

    def House(self, house):
        self.house = house
        return self.house
        

    def properties(self):
        return f"Name : {self.name} \nDegree: {self.degree}  \nCar: {self.car} \nhouse: {self.house}"
    
#builder function
class PersonBuilder:
    def addName(self):
        pass

    def addDegree(self):
        pass

    def addCar(self):
        pass

    def addhouse(self):
        pass

    def getData(self):
        pass

        
        



