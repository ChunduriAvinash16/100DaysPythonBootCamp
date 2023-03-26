# from data import question_data
from triviadata import question_data
from question_model import Question
from quiz_brain import  QuizBrain

question_bank = []
for question in question_data:
    question_bank.append(Question(question["question"], question["correct_answer"]))

# for question in question_bank:
#     print(f"{question.text}:{question.answer}")

q1 = QuizBrain(question_bank)
while q1.still_has_question():
    q1.next_question()

print("You've Completed the quiz")
print(f"Your final score is : {q1.score}/{q1.question_number}")