import json

filename = 'credentials.json'

# Handling the file storing login data, if the file does not exist,
# it asks the user to enter the login and password and creates a json file

try:
    with open(filename) as f_obj:
        json_obj = json.load(f_obj)
        user_login = json_obj['user_login']
        user_password = json_obj['user_password']
except FileNotFoundError:
    with open(filename, 'w') as f_obj:
        user_login = input('Enter LOGIN: ')
        user_password = input('Enter PASSWORD: ')
        credentials = {'user_login': user_login, 'user_password': user_password}
        json.dump(credentials, f_obj)
        print(f'Your login: {user_login} and password: {user_password} have been added.')
        f_obj.close()
