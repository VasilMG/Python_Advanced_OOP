from json import dumps, loads
users_db_path = ".\\users.txt"

def register(username, password):
    with open(users_db_path, 'r') as user_db:
        for line in user_db:
            info_user = loads(line.strip())
            if info_user['username'] == username:
                print('Enter Different username')
                return False

    with open(users_db_path, 'a') as user_db:
        user = {
            'username': username,
            'password': password,
            'products': []
        }
        user_json = dumps(user)
        user_db.write(user_json + '\n')
        return True

def login(username, password):
    with open(users_db_path, 'r') as user_db:
        for line in user_db:
            info_user = loads(line.strip())
            if info_user['username'] == username and info_user["password"] == password:
                with open('.\\current_user.txt', 'w') as current_user:
                    current_user.write(line)
                return True
        return False
def get_current_user():
    with open('.\\current_user.txt', 'r') as current_user_file:
        return loads(current_user_file.read().strip())