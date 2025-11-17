from .questions import questions  # Import the questions

import random

def ask_questions(num_questions):
    """
    Function to ask the quiz questions and track the score.
    Returns the user's score.
    Also displays feedback for each question.
    """
    score = 0
    # Shuffle the questions to display them in random order
    random.shuffle(questions)
    
    # Limit the number of questions to the user’s specified number
    for question, correct_answer in questions[:num_questions]:
        answer = input(question + " ").strip()

        # Check if the answer is correct
        if answer.lower() == correct_answer.lower():
            print("Correct!\n")
            score += 1
        else:
            print(f"Incorrect! The correct answer is: {correct_answer}\n")

    return score
