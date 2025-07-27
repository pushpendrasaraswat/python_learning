class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0



    def get_next_question(self):
        question = self.question_list[self.question_number]
        self.question_number += 1
        return question



    def has_more_questions(self):
        """
        Check if there are more questions to ask.
        Returns:
            bool: True if there are more questions, False otherwise.
        """
        return self.question_number < len(self.question_list)



    def check_answer(self, user_answer, correct_answer):
        """
        Check if the user's answer is correct.
        Args:
            user_answer (str): The answer provided by the user.
            Correct_answer (str): The correct answer to the question.
        Returns:
            bool: True if the answer is correct, False otherwise.
        """
        if user_answer.lower() == correct_answer.lower():
            print("Correct!")
            self.score += 1
        else:
            print("Wrong!")
        print("Correct answer was: ", correct_answer)
