from Source.Infrastructure.Repositories.UserRepository import *

class AuthService:

    def __init__(self):
        self.user_repository = UserRepository();

    def tryLogin(self, username, password):
       return self.user_repository.getUser(username)
