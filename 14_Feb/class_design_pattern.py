

#class 1
class Room:
    def __init__(self,length,width): # args
        self.length = length
        self.width = width
    
    def calculate_area(self):
        return "Area is:{} ".format(self.length * self.width)

r1 = Room(20,30)
res = r1.calculate_area()
print(res)
print("----------------------------------------------------")

#######################################################################################################################################
#class 2
class Car:
    def __init__(self,distance,time): #kwargs
        self.distance = distance
        self.time = time

    def find_speed(self):
        speed = self.distance // self.time
        return speed

s1 = Car(400,3)
res2 = s1.find_speed()
print("Speed is",res2)
print("----------------------------------------------------")


################################################################################################################################################
#class 3
class Student:
    def __init__(self, name,roll_no,age): #args
        self.name = name
        self.roll_no = roll_no
        self.age = age
        
    def show(self):
        return f"Welcome {self.name}! You have got the {self.roll_no}. Age:{self.age}"

st1 = Student("Sneha Saurav",1219311,21)
res3 = st1.show()
print(res3)
print("----------------------------------------------------")


###################################################################################################################################################
#class 4
class City:
    def __init__(self,*args): # postional arguments
        self.cityname = args[0]
        self.population = args[1]
        
    def details(self):
        return f"The {self.cityname} is having {self.population} population."

c1 = City('Noida',1700000)
res4 =c1.details()
print(res4)
print("----------------------------------------------------")


#####################################################################################################################################################

#class 5
class User():
    def __init__(self, **kwargs): #keywords arguments
        self.username = kwargs['u']
        self.password = kwargs['p']
        self.mobile_no= kwargs['m']
    
    def user_details(self):
        return f"Your username is {self.username} and password is {self.password} with mobile number {self.mobile_no}."
    
u1 = User(u='Sneha Saurav',p="Ssau123",m=9821778124)

res5 =u1.user_details()
print(res5)
print("----------------------------------------------------")



