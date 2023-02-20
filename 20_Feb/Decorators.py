import datetime
import csv
import maskpass
from cryptography.fernet import Fernet


Subjects =[]
#Password encrypter 
key = Fernet.generate_key()
f = Fernet(key)

def encrypt_password(password):
    b_pass = bytes(password,'UTF-8')
    encrypt_pass = f.encrypt(b_pass)
    return encrypt_pass


def is_valid_password(min_length):
    def inner(func):
        def decorator(first_name, Last_name, email,passwd,*args, **kwarg):
            SpecialSym =['$', '@', '#', '%']
            val = True
            
            if len(passwd) < min_length:
                print('length should be at least 6')
                val = False
                
            if len(passwd) > 20:
                print('length should be not be greater than 8')
                val = False
                
            if not any(char.isdigit() for char in passwd):
                print('Password should have at least one numeral')
                val = False
                
            if not any(char.isupper() for char in passwd):
                print('Password should have at least one uppercase letter')
                val = False
                
            if not any(char.islower() for char in passwd):
                print('Password should have at least one lowercase letter')
                val = False

            if not any(char in SpecialSym for char in passwd):
                print('Password should have at least one of the symbols $@#')
                val = False
            if val:
                return val
            return  func(first_name, Last_name, email,passwd,*args, **kwarg)
        return decorator
    return inner



#Email validation
def is_email_valid(func):
    def inner(first_name, Last_name, email,*args, **kwarg):
        # email = email.strip().lower()
        print(email)
        if not "@" in email:
            print("Invalid email")
            raise Exception("Invalid Email")
        elif not email[-4:] in ".com.org.edu.gov.net":
            print(email[-4:])
            print("Invalid email2")
            raise Exception("Invalid Email")
        return func(first_name, Last_name, email,*args, **kwarg)
    return inner
   
    
@is_email_valid
@is_valid_password(min_length=6)
def Register_user(first_name, Last_name, email,password,date_of_birth,subject,Class):
    #date of birth format:  
    birthdate  = datetime.datetime.strptime(date_of_birth, "%d/%m/%Y").date()
    today = datetime.date.today().year
    Age = int(today - birthdate.year)
    Subjects.append(subject)
    with open('./user.csv') as fp:
        csvreader = csv.reader(fp)
        fields = next(csvreader) # extract the field name 
        user = list(csvreader)
    email_exist = email in (item for sublist in user for item in sublist)
    print(email_exist)
    if email_exist:
        print("wrong")
        raise Exception("Already registered, Please Login")
    else:
        print("correct")
        with open('./user.csv', 'a', newline="") as fp:
            csvwrite =  csv.writer(fp)
            fields =['first_name','Last_name','Birth_Date','Email','Password','Subjects','class','Age']
            csvwrite.writerow(fields)
            data = [first_name, Last_name , date_of_birth, email, password ,Subjects,Class, Age]
            csvwrite.writerow(data)



while True:
    print("1. Register")
    print("2. Login")
    print("3. Exit")
    option  =int(input("Choose the options:"))
    if option == 1:
        first_name = input("First Name: ")
        Last_name = input("Last Name: ")
        date_of_birth = input("Date of Birth in (DD/MM/YYYY) format: ")
        email = input("Email: ")
        passwd = maskpass.askpass(prompt="Password:", mask="*")
        subject = input("Subject: ")
        Class = input("Class: ")
        res = Register_user(first_name, Last_name,email,passwd, date_of_birth,subject,Class)
        print(res)
        print("Registered Sucessfully!")
    elif option == 3:
        break
    else:
        print("Invalid Input")