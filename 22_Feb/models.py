import uuid 
import json
from json.decoder import *
import os


c_data =[]
blog_data=[]
data =[]
user ={}
blog ={}
comment ={}
def generate_uuid():
    id = uuid.uuid4()
    return str(id)


# def primary_key(func):
#         roll_no = 0 
#         def wrapper(*args, **kwargs):
#             nonlocal roll_no
#             roll_no += 1
#             return func(*args,pk=roll_no)
#         return wrapper





def primary_key(func):
        def wrapper(pk):
            with open('user.json', 'r')as fp:
                data = json.load(fp)
                print(data)
                for user in data:
                    if wrapper.pk == user['primary_key']:
                        # wrapper.pk+=1
                        pk +=1
                        print(type(wrapper.pk))
                return func(pk=wrapper.pk)
        # wrapper.pk = 1
        return wrapper
            

       
         

     

class User(object):
    def __init__(self, first_name, last_name, email, mobile_no, pk=None):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.mobile_no = mobile_no
        self.uuid = generate_uuid()

    @primary_key
    def set_user(self, pk=None):
        user['firstname'] = self.first_name
        user['lastname'] = self.last_name
        user['email'] = self.email
        user['mobile_no'] = self.mobile_no
        user['id'] = self.uuid
        user['primary_key'] = pk
        # print(pk)
        if os.path.isfile('user.json') and open('user.json').read(1):
                    print("ss")
                    with open('user.json', 'r')as fp:
                         data = json.load(fp)
        else:
            data = []
            user['primary_key'] = 1
        data.append(user)
        with open('user.json', "w",encoding='utf-8') as file:
                json.dump(data, file,separators=(',',': '))
                file.close()

    def intials(self):
        return self.first_name + "."+ self.last_name
    
    @classmethod
    def getallUser(self):
         with open('user.json', 'r')as fp:
            data = json.load(fp)
            return data

    

class Blog(object):
    def __init__(self, title , body , create_date, user):
        self.user = user
        self.title = title
        self.body = body
        self.create_date = create_date

    def set_blog(self):
        blog['user'] = self.user
        blog['title'] = self.title
        blog['body'] = self.body
        blog['create_date'] = self.create_date
        blog['id'] = generate_uuid()
        # print(self)
        if os.path.isfile('blog.json') and  open('blog.json').read(1):
                    print("ss")
                    with open('blog.json', 'r')as fp:
                        blog_data = json.load(fp)
        else:
             blog_data = []
        blog_data.append(blog)
        with open('blog.json', "w",encoding='utf-8') as file:
                json.dump(blog_data, file,separators=(',',': '))
                file.close()



    @classmethod
    def getallBlog(self):
         with open('blog.json', 'r')as fp:
            data = json.load(fp)
            return data


class Comments(object):
    def __init__(self, comment , blog):
        self.blog = blog
        self.comment = comment
    

    def set_comment(self):
        comment['blog'] = self.blog
        comment['comment'] = self.comment
        comment['id'] = generate_uuid()
        if os.path.isfile('comment.json') and  open('comment.json').read(1):
                    with open('comment.json', 'r')as fp:
                        c_data = json.load(fp)
        else:
             c_data = []
        print(comment)
        c_data.append(comment)
        with open('comment.json', "w",encoding='utf-8') as file:
                json.dump(c_data, file,separators=(',',': '))
                file.close()
    
    @classmethod
    def getallComment(self):
         with open('comment.json', 'r')as fp:
            data = json.load(fp)
            return data



    

# u1 = User('SanSnehaya','Arora','sneha@gmail.com','9837238585')
# print(u1.__dict__)
# u1.set_user()
# u2 = User('Sanya','Arora','sneha@gmail.com','9837238585')
# u2.set_user()
# print(json.dumps(u1.getallUser(), indent=4))
# print("____________________________________________________________________________________________________________________")
# b1 = Blog('sdd','jdjded','jdjded', u1)
# b1.set_blog()
# print(json.dumps(b1.getallBlog(), indent=4))

# c1 = Comments('Nice!', b1, u1)
# c1.set_comment()

