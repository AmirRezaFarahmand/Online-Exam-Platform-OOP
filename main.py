class User:
    def __init__(self, name, email):
        self.user_id = 0
        self.name = name
        self.email = email

    def display_info(self):
        print('name: ', self.name, ', email: ', self.email)

