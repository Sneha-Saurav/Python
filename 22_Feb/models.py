import random 
import json
c_data =[]
blog_data=[]
user ={}
blog ={}
def generate_uuid():
    id = random.randint(1,100000)
    return id


class User(object):
    def __init__(self, first_name, last_name, email, mobile_no, uuid):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.mobile_no = mobile_no
        self.uuid = generate_uuid()

    
    def set_user(self):
        user['firstname'] = self.first_name
        user['lastname'] = self.last_name
        user['email'] = self.email
        user['mobile_no'] = self.mobile_no
        user['id'] = self.uuid
        with open('user.json')as fp:
             data = json.load(fp)
        data.append(user)
        with open('user.json', "w") as file:
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
        blog['user'] = self.user.__dict__
        blog['title'] = self.title
        blog['body'] = self.body
        blog['create_date'] = self.create_date
        blog['id'] = generate_uuid()
        with open('blog.json')as fp:
            blog_data = json.load(fp)
        blog_data.append(blog)
        with open('blog.json', "w") as file:
             json.dump(blog_data, file,separators=(',',': '))
             file.close()


    @classmethod
    def getallBlog(self):
         with open('blog.json', 'r')as fp:
            data = json.load(fp)
            return data


class Comments(object):
    def __init__(self, comment , blog ,  user):
        self.user = user
        self.blog = blog
        self.comment = comment
    

    def set_comment(self):
        blog['user'] = self.user.__dict__
        blog['blog'] = self.blog.__dict__
        blog['comment'] = self.comment
        blog['id'] = generate_uuid()
        # with open('comment.json')as fp:
        #     c_data = json.load(fp)
        # c_data.append(blog)
        with open('comment.json', "w") as file:
            #  c_data = json.load(file)
             c_data.append(blog)
             json.dump(c_data, file,separators=(',',': '), indent=4)
             file.close()


    

u1 = User('fggf','Saurav','sneha@gmail.com','9837238585', 29)
data = u1.set_user()
print(json.dumps(u1.getallUser(), indent=4))
print("____________________________________________________________________________________________________________________")
b1 = Blog('sdd','jdjded','jdjded', u1)
b1.set_blog()
print(json.dumps(b1.getallBlog(), indent=4))

# c1 = Comments('Nice!', b1, u1)
# c1.set_comment()



#create id using uuid 
# create primary key using increment with decorator