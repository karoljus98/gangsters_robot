import json
from getpass import getpass

filename = 'credentials.json'
flag = True
# Handling the file storing login data, if the file does not exist,
# it asks the user to enter the login and password and creates a json file

try:
    with open(filename) as f_obj:
        json_obj = json.load(f_obj)
        user_login = json_obj['user_login']
        user_password = json_obj['user_password']
except FileNotFoundError:
    while flag:
        with open(filename, 'w') as f_obj:
            user_login = input('Enter LOGIN: ')
            user_password = getpass(prompt='Enter PASSWORD: ', stream=None)
            user_password2 = getpass(prompt='Reenter PASSWORD: ', stream=None)
            if user_password == user_password2:
                credentials = {'user_login': user_login, 'user_password': user_password}
                json.dump(credentials, f_obj)
                f_obj.close()
                flag = False
            elif user_password != user_password2:
                print('The passwords do not match! Try again!')
