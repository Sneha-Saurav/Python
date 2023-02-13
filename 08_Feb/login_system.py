import datetime
import csv
import re
import maskpass
from cryptography.fernet import Fernet



Subjects =[]
#Email pattern
regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
fields =['First Name', 'Last Name' , 'Date of Birth', 'Email', 'Password' ,'Subjects','Class', 'Age']
r_p = r'[A-Za-z0-9@#$%^&+=]{8,}'

#Password encrypter 
key = Fernet.generate_key()
f = Fernet(key)

def encrypt_password(password):
    b_pass = bytes(password,'UTF-8')
    encrypt_pass = f.encrypt(b_pass)
    return encrypt_pass


def is_valid_password(password):
    if re.fullmatch(r_p,password):
        print("correct")
        return password
    else:
        raise Exception("Invalid Format of Password")
        
#Email validation
def is_valid(email):
    if  re.fullmatch(regex,email):
        return email
    else:
        print("wrong")
        raise Exception("Invalid Email")
def Register_user():
    first_name = input("First Name: ")
    Last_name = input("Last Name: ")
    date_of_birth = input("Date of Birth in (DD/MM/YYYY) format: ")
    email = input("Email: ")
    password = maskpass.askpass(prompt="Password:", mask="*")
    subject = input("Subject: ")
    Class = input("Class: ")
    #date of birth format:  
    birthdate  = datetime.datetime.strptime(date_of_birth, "%d/%m/%Y").date()
    today = datetime.date.today().year
    Age = int(today - birthdate.year)
    Subjects.append(subject)
    valid_email =is_valid(email)
    print(valid_email)
    valid_password = is_valid_password(password)
    password = encrypt_password(valid_password)
    print(password)
    #read the list
    with open('user.csv') as fp:
        csvreader = csv.reader(fp)
        fields = next(csvreader) # extract the field name 
        user = list(csvreader)

    email_exist = valid_email in (item for sublist in user for item in sublist)
    print(email_exist)
    if email_exist:
        print("wrong")
        raise Exception("Already registered, Please Login")
    else:
        print("correct")
        with open('user.csv', 'a', newline="") as fp:
            csvwrite =  csv.writer(fp)
            data = [first_name, Last_name , date_of_birth, valid_email, password ,Subjects,Class, Age]
            csvwrite.writerow(data)

def Login_user():
    with open('user.csv') as fp:
        csvreader = csv.reader(fp)
        fields = next(csvreader) # extract the field name 
        user = list(csvreader)
    print(user)
    email = input("Email: ")
    password = maskpass.askpass(prompt="Password:", mask="*")
    valid_email =is_valid(email)
    print(valid_email)
    valid_password = is_valid_password(password)
    password = encrypt_password(valid_password)
    email_exist = valid_email in (item for sublist in user for item in sublist)

    if email_exist:
        password_match = valid_password in (item for sublist in user for item in sublist)
        if password_match:
            res =  "Login Successfully!"
        else:
            raise Exception("Wrong Credentials!")
    else:
        raise Exception("Email not found , Please register")
    
    return res

while True:
    print("1. Register")
    print("2. Login")
    print("3. Exit")

    option  =int(input("Choose the options:"))
    if option == 1:
        res = Register_user()
        print("Registered Sucessfully")
        #register
    elif option == 2:
        res =Login_user()
        print(res)
    elif option == 3:
        break
    else:
        print("Invalid Input")