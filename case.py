class Automation:

    def __init__(self, assignment, quizzes, final_exam, total_items_assn, total_items_quizzes):
        self.assignment = assignment
        self.quizzes = quizzes
        self.final_exam = final_exam
        self.total_items_assn = total_items_assn
        self.total_items_quizzes = total_items_quizzes

    def calculate_weighted_average(self):
        assignment_weight = 0.3
        quiz_weight = 0.3
        final_exam_weight = 0.4

        total_assn = (sum(self.assignment) / self.total_items_assn) * 100
        total_quiz = (sum(self.quizzes) / self.total_items_quizzes) * 100
        weighted_avg = (total_assn * assignment_weight) + (total_quiz * quiz_weight) + (self.final_exam * final_exam_weight)

        return weighted_avg

    def assign_letter_grade(self):

        if 90 <= self.weighted_avg <= 100:
            return 'A'
        elif 80 <= self.weighted_avg < 90:
            return 'B'
        elif 70 <= self.weighted_avg < 80:
            return 'C'
        elif 60 <= self.weighted_avg < 70:
            return 'D'
        else:
            return 'F'






assn = input("Enter assignment scores separated by spaces:  ")
assn_list = list(map(int, assn.split()))  # List maker and separates the number from spaces
total_items_assn = int(input("Give the total items of all the Assignments: "))

quizzes = input("Enter quizzes scores separated by spaces:  ")
quiz_list = list(map(int, quizzes.split()))
total_items_quiz = int(input("Give the total items of all the Quizzes: "))

final_exam = int(input("Enter total score in the Final Exam: "))



a = Automation(assn_list, quiz_list, final_exam, total_items_assn, total_items_quiz)
# b = print(a.calculate_weighted_average())  #Find out on how you can print the letter value ok?
# print(a.assign_letter_grade())


