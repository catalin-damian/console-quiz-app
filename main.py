from quiz.quiz_logic import ask_questions, questions

def display_menu():
    """
    Displays the main menu with options to start the quiz or exit.
    """
    print("Welcome to the Quiz App!")
    print("1. Start the Quiz")
    print("2. Exit")

def get_user_name():
    """
    This function prompts the user to enter their name.
    It keeps asking until a non-empty, valid name (only letters) is provided.
    """
    while True:
        name = input("Please enter your name: ").strip()
        
        # First, check if the name is empty
        if not name:
            print("Name field can't be empty. Please try again.")
        # Then, check if the name contains only alphabetic characters
        elif not name.isalpha():
            print("Name field must contain only letters. Please try again.")
        else:
            print(f"Welcome, {name}!\n")  # Greets the user
            return name

def get_number_of_questions():
    """
    Asks the user how many questions they want to answer.
    Returns the number of questions (ensuring it's valid).
    If the user enters a number greater than the available questions, prompts again.
    """
    while True:
        try:
            num_questions = int(input(f"How many questions would you like to answer? (1 to {len(questions)}): ").strip())
            
            # Ensure the number is within the valid range
            if num_questions < 1:
                print("Please enter a number greater than 0.")
            elif num_questions > len(questions):
                print(f"You've entered {num_questions}. We only have {len(questions)} questions available. Please enter a number between 1 and {len(questions)}.")
            else:
                return num_questions  # Return the valid number of questions
        
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def main():
    """
    Main function to run the quiz app.
    Displays the menu, asks for user input, starts the quiz if selected, or exits if chosen.
    """
    user_scores = []  # List to store users' names and their scores

    while True:
        display_menu()
        choice = input("Please select an option (1 to start quiz, 2 to exit): ").strip()

        if choice == "1":
            # If user chooses to start the quiz, ask for their name
            user_name = get_user_name()
            print(f"Starting the quiz for {user_name}...\n")

            # Ask how many questions the user wants to answer
            num_questions = get_number_of_questions()
            
            # Ask the questions and get the score
            score = ask_questions(num_questions)

            # Store the user’s name and score
            user_scores.append((user_name, score))

            # Display the results for this user
            print(f"\n{user_name}, your final score is {score} out of {num_questions}.")
            percentage = (score / num_questions) * 100
            print(f"Your percentage is: {percentage:.2f}%\n")
            
            # Ask if another user wants to take the quiz
            another_user = input("Would another user like to take the quiz? (yes/no): ").strip().lower()
            if another_user != 'yes':
                break  # Exit the loop if no more users want to take the quiz

        elif choice == "2":
            print("Exiting the Quiz App. Goodbye!")
            break  # Exit the program
        
        else:
            print("Invalid option. Please select 1 to start or 2 to exit.")
    
    # After all users have completed the quiz, display the overall results
    display_overall_results(user_scores)

def display_overall_results(user_scores):
    """
    Function to display the overall quiz results.
    Shows the user with the highest score and the average score of all users.
    """
    if not user_scores:
        print("No users have completed the quiz.")
        return

    # Calculate highest score
    highest_score_user = max(user_scores, key=lambda x: x[1])
    highest_score_name, highest_score = highest_score_user
    print(f"\nThe highest score was achieved by {highest_score_name} with a score of {highest_score}.")

    # Calculate average score
    total_score = sum(score for _, score in user_scores)
    average_score = total_score / len(user_scores)
    print(f"The average score of all users is: {average_score:.2f}")


# Entry point of the program
if __name__ == "__main__":
    main()
