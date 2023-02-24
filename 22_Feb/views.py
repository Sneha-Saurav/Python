import os
from models import User, Blog, Comments
import json

def  get_all_user(user):
    print("start")
    json_user = json.dumps(user, indent=4)
    return json_user


def create_user(req_user):
    try:
        u1 = User(req_user['first_name'], req_user['last_name'], req_user['email'], req_user['mobile_no'])
        u1.set_user()
    except Exception as e:
        raise Exception(e)
    print("Successfully Created")

def get_user(users, id):
    user =[user for user in users if user['id'] == id]
    json_user = json.dumps(user, indent=4)
    return json_user

# def delete_userView(users, id):
#     try:
#         index =[idx for idx,user in enumerate(users) if user['id'] == id]
#         with open('user.json', 'r')as fp:
#                 print(index)
#                 data = json.load(fp)
#                 data.pop(index)
#         return "Successfully Deleted"
#     except Exception as e:
#         raise Exception(e)

def create_blog(req_user, user):
    try:
        if os.path.isfile('blog.json') and  open('blog.json').read(1):
            user = json.loads(user)
            print(type(user))
            b1 = Blog(req_user['title'], req_user['body'], req_user['created_date'],user[0])
            b1.set_blog()
    except Exception as e:
        raise Exception(e)
    print("Successfully Created Blog")


def get_all_blogView(blogs):
    json_blog = json.dumps(blogs, indent=4)
    return json_blog

def get_blog(blogs, id):
    blog =[blog for blog in blogs if blog['id'] == id]
    json_user_blog = json.dumps(blog, indent=4)
    return json_user_blog


def get_all_blog_usersView(blog , id):
    data =[]
    for b in blog:
        if b['user']['id'] == id:
            data.append(b)
    json_data= json.dumps(data, indent=4)
    return json_data
    

def create_comment(req_comment, blog):
    try:
        if os.path.isfile('comment.json') and  open('comment.json').read(1):
                blog = json.loads(blog)
                b1 = Comments(req_comment['comment'],blog)
                print(b1)
                b1.set_comment()
    except Exception as e:
        raise Exception(e)
    print("Successfully Created Comment")

def get_All_commentView(comments):
    json_blog = json.dumps(comments, indent=4)
    return 


def get_allcomment_blogView():
    pass









