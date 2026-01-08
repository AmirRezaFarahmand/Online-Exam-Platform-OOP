class User:
    def __init__(self, name, email):
        self.user_id = 0
        self.name = name
        self.email = email

    def set_user_id(self, last_user_id):
        self.user_id = last_user_id + 1

    def display_info(self):
        print('name: ', self.name, ', email: ', self.email)

class Admin(User):
    def __init__(self, name, email):
        super().__init__(name, email)
        self.created_exams = []

    def create_exam(self, title, description, duration):
        new_exam = Exam(title, description, duration)
        self.created_exams.append(new_exam)
        new_exam.set_exam_id(len(self.created_exams))
        return new_exam

    def add_question(self, exam, question):
        exam.add_question(question)

    def list_exams(self):
        for exam in self.created_exams:
            print(exam.title,
                  ' | Desc: ', exam.description,
                  ' | Duration: ', exam.duration,
                  ' | Questions: ', len(exam.questions),
                  ' | Published: ', 'Yes' if exam.is_published() else 'No' )

class Student(User):
    def __init__(self, name, email):
        super().__init__(name, email)
        self.taken_exams = {}

    def list_available_exams(self, all_exams):
        for exam in all_exams:
            if exam.is_published():
                print(exam.title,
                      ' | Desc: ', exam.description,
                      ' | Duration: ', exam.duration,
                      ' | Questions: ', len(exam.questions),
                      ' | Score: ', self.taken_exams[exam] if exam in self.taken_exams else 'Not taken' )

    def take_exam(self, exam):
        print(exam.title, ' | Duration: ' , exam.duration, " , Good luck!")
        correct_answers = 0
        total_points = 0
        for question in exam.questions:
            question.display()
            student_answer = input('Answer: ')
            total_points += question.points
            if question.check_answer(student_answer):
                correct_answers += question.points
        final_score = correct_answers / total_points
        self.taken_exams[exam] = final_score
        print('Your final score is: ', final_score)


    def view_results(self):
        for exam, score in self.taken_exams:
            print(exam.title,
                  ' | Score: ', score)

class Exam:
    def __init__(self, title, description, duration):
        self.exam_id = 0
        self.title = title
        self.description = description
        self.duration = duration
        self.questions = []
        self.is_published = False

    def set_exam_id(self, last_exam_id):
        self.exam_id = last_exam_id + 1

    def add_question(self, question):
        self.questions.append(question)

    def conduct_exam(self, student):
        student.take_exam(self)

    def change_published_status(self, status):
        self.is_published = status

class Question:
    def __init__(self, question_text, points):
        self.question_id = 0
        self.question_text = question_text
        self.points = points

    def set_question_id(self, last_question_id):
        self.question_id = last_question_id + 1

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

    def set_correct_option(self, correct_option):
        correct_option = int(correct_option)
        self.correct_option = correct_option

class TFQ(Question):
    def __init__(self, question_text, points):
        super().__init__(question_text, points)
        self.correct_answer = False

    def display(self):
        print(self.question_text, " (True/False)")

    def to_bool(self, answer):
        if answer == "T" or answer == "t" \
                or answer == "true" or answer == "True" \
                or int(answer) == 1:
            return True
        return False

    def check_answer(self, user_answer):
        return self.to_bool(user_answer) == self.correct_answer

    def set_correct_answer(self, correct_answer):
        self.correct_answer = self.to_bool(correct_answer)

