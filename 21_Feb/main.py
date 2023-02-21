from Builder import Person, PersonBuilder

class EmployeeBuilder(PersonBuilder):
    def __init__(self):
        self.person = Person()

    def addName(self):
         self.person.Name('Sneha')
         return self
    
    def addDegree(self):
        self.person.Degree('B.Tech')
        return self

    def addCar(self):
        self.person.Car('i20')
        return self

    def addhouse(self):
        self.person.House('Flat')
        return self
    
    def getData(self):
        return self.person
    

class Director:
    def __init__(self, person_builder):
        self.person_builder = person_builder

    def get_person(self):
        return self.person_builder.addName().addDegree().addCar().addhouse().getData()


builder = EmployeeBuilder()
director = Director(builder)
emp = director.get_person()


print(emp.properties())

    


