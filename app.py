import datetime
from users_models import UserBaseClass

print('**********************************************************')
print('Hello, welcome to spearhead. Experience the power of code')
print('***********************************************************')
print('Please enter your email and password to login')

email = input('Email: ')
password = input('Password: ')
user = UserBaseClass(1, 'email@email.com', 'passoword')
if user.verify():
    print(user.log_in())
else:
    print('Wrong password')

    