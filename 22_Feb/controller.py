import datetime
from models import User, Blog , Comments
import views

def Show_alluser():
    users = User.getallUser()
    return views.get_all_user(users)

def request_user():
    request={}
    print("To create the user , input your data:")
    request['first_name'] = input('Enter your first name:')
    request['last_name'] = input('Enter your last name:')
    request['email'] = input("Enter you email:")
    request['mobile_no'] = input("Enter your mobilr number:")
    return views.create_user(request)


def one_user():
    users = User.getallUser()
    id = input('Enter the id:')
    return views.get_user(users, id)


def delete_user():
    id = input('Enter the id want to delete:')
    users = User.getallUser()
    return views.delete_userView(users, id)


def request_blog():
    request={}
    print("To create the user , input your data:")
    request['user'] = input('Enter the user id:')
    request['title'] = input('Enter your title:')
    request['body'] = input("Enter you body:")
    request['created_date'] = str(datetime.date.today())
    list_user = User.getallUser()
    user = views.get_user(list_user, request['user'])
    return views.create_blog(request, user)

def Show_allBlogs():
    blog = Blog.getallBlog()
    return views.get_all_blogView(blog)

def one_blog():
    blogs = Blog.getallBlog()
    id = input('Enter the id:')
    return views.get_blog(blogs, id)


def get_all_blog_users():
    id =  input("Enter the user id")
    blog = Blog.getallBlog()
    return views.get_all_blog_usersView(blog, id)

def add_comment():
    request ={}
    request['blog'] = input("Enter your blog id: ")
    request['comment'] = input("Enter the comment: ")
    list_blog = Blog.getallBlog()
    blog = views.get_blog(list_blog, request['blog'])
    return views.create_comment(request, blog)

def get_comment():
    comment = Comments.getallComment()
    return views.get_All_commentView(comment)

def get_allcomment_blog():
    comments = Comments.getallComment()
    id =  input("Enter the blog id")
    return views.get_allcomment_blogView(comments,id)
    
if __name__ == '__main__':
    # print(get_all_blog_users())
    # add_comment()
    # print(get_comment())
    # while True:
    #     print("1. User")
    #     print("2. Blog")
    #     print("3. Comments")
    #     print("4. Exit")
         
    #     option  = input("Enter your choice: ")
    #     if option ==1:
    #         print("1. Create user")
    #         print("2. Get All user")
    #         print('3. Get user')
    #         print("4. Exit")
    #         user_option = input("Enter the user choice: ")
    #         if option == 1:
    #             print(request_user())
    #         elif option == 2:
    #             print(Show_alluser())
    #         elif option == 3:
    #             print(one_user())
    #         elif option == 4:
    #             break
    #         else:
    #             print("Invalid Input")
    #     elif option == 2:
    #         print("1. Create blog")
    #         print("2. Get All blog")
    #         print('3. Get blog')
    #         print("4. Exit")
    #         user_option = input("Enter the user choice: ")
    #         if option == 1:
    #             print(request_blog())
    #         elif option == 2:
    #             print(Show_allBlogs())
    #         elif option == 3:
    #             print(one_blog())
    #         elif option == 4:
    #             break
    #         else:
    #             print("Invalid Input")
    #     elif option == 3:
    #         print("1. Add Comment to Blog")
    #         print("2. Get Comment")
    #         print("3. Get all comments of Blog")
    #         print("4. Exit")
    #         if option == 1:
    #             print(add_comment())
    #         elif option == 2:
    #             print(get_comment())
    #         elif option==3:
    #             pass
    #         elif option ==4:
    #             break

    request_user()

            






            
