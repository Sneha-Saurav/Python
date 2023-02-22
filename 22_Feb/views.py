from models import User, Blog
import json

def ShowAllUser(user):
    print("start")
    json_user = json.dumps(user, indent=4)
    print(json_user)


def request_user(req_user):
    print(req_user['first_name'])
    u1 = User(req_user['first_name'], req_user['last_name'], req_user['email'], req_user['mobile_no'])
    return u1.set_user()


