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

class Question:
    def __init__(self, question_text, points):
        self.question_id = 0
        self.question_text = question_text
        self.points = points

    def display(self):
        print(self.question_text)

    def check_answer(self, user_answer):
        print(user_answer == self.question_text)

class MCQ(Question):
    def __init__(self, question_text, points):
        super().__init__(question_text, points)
        self.options = []
        self.correct_option = 0

    def display(self):
        print(self.question_text)
        for i in range(len(self.options)):
            print(i + 1, ": ", self.options[i])

    def check_answer(self, user_choice):
        user_choice = int(user_choice)
        return user_choice == self.correct_option

class TFQ(Question):
    def __init__(self, question_text, points):
        super().__init__(question_text, points)
        self.correct_answer = False

    def display(self):
        print(self.question_text, " (True/False)")

    def check_answer(self, user_answer):
        if user_answer == "T" or user_answer == "t" \
            or user_answer == "true" or user_answer == "True" \
            or int(user_answer) == 1:
            user_answer = True
        else:
            user_answer = False
        return user_answer == self.correct_answer

    