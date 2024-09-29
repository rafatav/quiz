from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for new_q in question_data:
    question_bank.append(Question(new_q["text"], new_q["answer"]))

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")