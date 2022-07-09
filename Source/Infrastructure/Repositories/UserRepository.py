class UserRepository:
    def __init__(self):
        self.users = {
            'jose' : {'username': 'jose', 'password': 123}
        }

    def getUser(self, username):
        try:
            return self.users[username]
        except KeyError:
            return {}