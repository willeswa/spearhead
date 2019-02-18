from users_models import UserBaseClass, Moderator, Admin, Comments
import datetime

print('**********************************************************')
print('Hello, welcome to spearhead. Experience the power of code')
print('***********************************************************')
print('Please enter your email and password to login')


user = UserBaseClass('email@email.com', 'passoword')
mod = Moderator('email', 'password')
admin = Admin('email', 'password')

email = input('Email: ')
password = input('Password: ')

if user.verify(email, password):
    user.log_in()
    print(user.last_logged_in_at)
    choice = input('Select: 1. To create a comment\n 2. Edit comment\n 3. Deelete comment \n or q to logout')
    if choice == '1':
        Comments('message', 'author', datetime.datetime.timestamp, 'name').create_comment()
    elif choice == 2:
        pass
else:
    print('Invalid email or password')