import time
real_password = '999a'
my_list = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_+'
password_found = False
my_guess = ''
for i in my_list:
    my_guess = i
    if my_guess == real_password:
        password_found = True
        print('Password is', my_guess)
        break

for i1 in my_list:
    for i2 in my_list:
        my_guess = i1 + i2
        if my_guess == real_password:
            password_found = True
            print('Password is', my_guess)
            break
    if password_found == True:
        break


