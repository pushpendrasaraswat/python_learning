from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

def create_question_bank():
    """
    Create a list of Question objects from the question data.
    Returns:
        list: A list of Question objects.
    """
    question_bank = []
    for item in question_data:
       question_bank.append(Question(item["text"], item["answer"]))
    return question_bank



def start_questions():
    start_question_index = 1
    """
    Start the quiz by iterating through the questions and printing them.
    """
    while quiz_brain.has_more_questions():
        question = quiz_brain.get_next_question()
        user_answer = input(f"Q{start_question_index}: {question.text} (True/False):")

        quiz_brain.check_answer(user_answer, question.answer)

        start_question_index += 1
        print(f"your current score is: {quiz_brain.score}/{quiz_brain.question_number}")
        print("\n"*5)

    print("Thank you for playing!")
    print(f"your final score is: {quiz_brain.score}/{quiz_brain.question_number}")

quiz_brain = QuizBrain(create_question_bank())
start_questions()










