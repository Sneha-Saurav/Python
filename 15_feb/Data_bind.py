# Data Bind


# class Student:
#     def display(self):
#         print(self.name)


# res = Student() # it will give address
# print(res)


def User(firstname, lastname):
    return "Welcome {} {}.Welcome to Net Solutions".format(firstname, lastname)

def User(firstname, lastname, username):
    return "Welcome {} {}!! Your username is: {}".format(firstname, lastname,username)


# print(User("Sneha", "Saurav"))    # shows error 
print(User("Sneha", "Saurav", 'Sneha-20'))
print("_______________________________________________")


# Using args and kwargs
def Sum(*args):
    sum =0
    for i in args:
        sum  = sum + i
    return sum

print(Sum(1,2))
print("________________________________________")
print(Sum(1,2,4,5,7))


def User_details(**data):       # it store data as a dictionary
    # print(data.items())
    for key, value in data.items():
        print("{} is {}".format(key, value))


User_details(name='Sneha', username='Sneha-Saurav20')
print("___________________________________")
User_details(name='Yashika', username='Yashika20',date_of_birth="20 August")




