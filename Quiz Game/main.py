from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for i in question_data:
    question_bank.append(Question(i["question"], i["correct_answer"]))

quiz = QuizBrain(question_bank)
quiz.next_question()

while quiz.still_has_questions():
    quiz.next_question()

print("You have completed the Quiz!")
print(f"Your Final score is: {quiz.score}/{quiz.question_number}.")
