from sys import implementation


class User:
    def __init__(self, name, email):
        self.user_id = 0
        self.name = name
        self.email = email

    def display_info(self):
        print('name: ', self.name, ', email: ', self.email)

class Admin(User):
    def __init__(self, name, email):
        super().__init__(name, email)
        self.created_exams = []

    def create_exam(self, title, duration):
        pass

    def add_question(self, question):
        pass

    def list_exams(self):
        pass