# dictionary 

users =[]

dict = {}
dict['subject'] =[]

def student_list(users):
    return users

def update(users):
    id = int(input("Enter the Roll number:"))
    name = input("Enter the name:")
    subject = input("Enter the subject:")
    Class = input("Enter the class:")

    for i in users:
        if i['roll_no'] == id:
            dict['name'] =  name
            dict['subject'].append(subject)
            dict['class'] =  Class
        

def search(users):
    name = input("Enter the name: ")
    for i in users:
        if i['name'] == name:
            user = i
        else:
            user = None
    return user

def delete_student(users):
    id = int(input("Enter the roll number:"))
    for i in users:
        if i['roll_no'] == id:
            users.remove(i)
    



def add_student():
    roll_no = int(input("Enter the Roll number:"))
    name = input("Enter the name: ")
    subject = input("Enter the subject:")
    Class = input("Enter the class:")

    dict['roll_no'] =roll_no
    dict['name']=name
    dict['subject'].append(subject)
    dict['class'] = Class

    users.append(dict)
    return dict

while True:
    
    print("1. List the Student list")
    print("2. Search Student ")
    print("3. Update Student")
    print("4. Delete Student")
    print("5. Add Student")
    print("6. Exit")
    option = int(input("Please Choose One Options:"))
    if option  == 1:
        res = student_list(users)
        print(res)
    elif option == 2:
        res = search(users)
        print(res)
    elif option == 3:
        res = update(users)
        print("Update sucessfully")
    elif option == 4:
        delete_student(users)
        print("Deleted Successfully")
    elif option == 5:
        res = add_student()
        print("Added Successfully")
    elif option == 6:
       break
    else:
        print("Invalid option")





