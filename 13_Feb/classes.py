#class 1

class Room:
    length = 0
    width = 0
    height = 0

    def calculate_area(self):
        return self.length* self.width

r1 = Room()
r1.length = 20
r1.width = 40
res = r1.calculate_area()
print("Area is ",res)

#######################################################################################################################################
#class 2
class Car:
    distance = 0
    time = 0

    def find_speed(self):
        speed = self.distance // self.time
        return speed

s1 = Car()
s1.distance = 200
s1.time = 2
res2 = s1.find_speed()
print("Speed is",res2)

################################################################################################################################################
#class 3
class Student:
    name=""
    roll_no=0
    age = 0
    def Show(self):
        return f"Welcome {self.name}! You have got the {self.roll_no}."

st1 = Student()
st1.name = "Sneha Saurav"
st1.roll_no = "1219311"
st1.age = 22
res3 = st1.Show()
print(res3)

###################################################################################################################################################
#class 4
class City:
    cityname =''
    population=0

    def details(self):
        return f"The {self.cityname} is having {self.population} population."

c1 = City()
c1.cityname = "Noida"
c1.population = 1200000
res4 =c1.details()
print(res4)

#####################################################################################################################################################

#class 5
class User():
    username = ""
    password = ''
    mobile_no= 0
    
    def user_details(self):
        return f"Your username is {self.username} and password is {self.password} with mobile number {self.mobile_no}."
    
u1 = User()
u1.username = "sneha.saurav20"
u1.password = 'wfh@123456'
u1.mobile_no = 98217761611
res5 =u1.user_details()
print(res5)


