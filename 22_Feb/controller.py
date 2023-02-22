from models import User, Blog
import views

def Show_alluser():
    users = User.getallUser()
    return views.ShowAllUser(users)

def create_user():
    request={}
    print("To create the user , input your data:")
    request['first_name'] = input('Enter your first name')
    request['last_name'] = input('Enter your last name')
    request['email'] = input("Enter you email")
    request['mobile_no'] = input("Enter your mobilr number")
    return views.request_user(request)




if __name__ == '__main__':
    create_user()

    Show_alluser()