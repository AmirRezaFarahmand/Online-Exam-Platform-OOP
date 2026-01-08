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

class Student(User):
    def __init__(self, name, email):
        super().__init__(name, email)
        self.taken_exams = []

    def list_available_exams(self):
        pass

    def take_exam(self, exam):
        pass

    def view_results(self):
        pass


class Exam:
    def __init__(self, title, description, duration):
        self.exam_id = 0
        self.title = title
        self.description = description
        self.duration = duration
        self.is_published = False

    def add_question(self, question):
        pass

    def conduct_exam(self, student):
        pass

