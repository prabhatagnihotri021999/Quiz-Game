from Data import question_data

class Question:

    def __init__(self, question_data):
        self.score = 0
        self.question_no = 0
        self.questions = question_data

    def print_question(self):
        print(self.questions[self.question_no]['question'],"(True/False):")

    def take_input(self):
        self.user_answer = input()

    def check_answer(self):
        if((self.questions[self.question_no]['correct_answer'].lower()) == self.user_answer.lower()):
            self.score += 1
            print('You got it right!')
            print('The correct answer was',self.questions[self.question_no]['correct_answer'])
            self.question_no += 1
            print('your current score is', self.score,'/', self.question_no)
        else:
            print("That's a wrong answer")
            print('The correct answer was', self.questions[self.question_no]['correct_answer'])
            self.question_no += 1
            print('your current score is', self.score, '/', self.question_no)




