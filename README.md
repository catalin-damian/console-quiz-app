
                        CONSOLE QUIZ APP - USER MANUAL

1. OVERVIEW
------------------------------------------------------------------------------
The Console Quiz App is a Python-based command-line application that allows 
users to test their general knowledge. It supports multiple users in a single 
session, tracks individual scores, and calculates overall statistics (highest 
score and average score) upon exit.

2. PROJECT STRUCTURE
------------------------------------------------------------------------------
Ensure your files are organized in the following folder structure for the 
application to run correctly:

console_quiz_app/             <-- Root Directory
│
├── main.py                   <-- The entry point of the application
│
└── quiz/                     <-- Package folder containing logic
    ├── __init__.py           (Required to treat the directory as a package)
    ├── questions.py          (Database of questions and answers)
    └── quiz_logic.py         (Functions handling the game mechanics)

3. PREREQUISITES
------------------------------------------------------------------------------
- Python 3.x installed on your machine.
- No external third-party libraries are required (uses standard 'random' library).

4. HOW TO RUN THE APPLICATION
------------------------------------------------------------------------------
1. Open your terminal or command prompt.
2. Navigate to the root directory of the project ('console_quiz_app').
3. Run the following command:

   python main.py

5. USER INSTRUCTIONS
------------------------------------------------------------------------------
Once the application is running, follow these steps:

Step 1: Main Menu
   - Select '1' to Start the Quiz.
   - Select '2' to Exit the application.

Step 2: User Registration
   - Enter your name when prompted.
   - Note: The name must contain only letters and cannot be empty.

Step 3: Select Quiz Length
   - Choose how many questions you wish to answer.
   - The input must be a number between 1 and the total number of available 
     questions (currently 20).

Step 4: Taking the Quiz
   - Questions will appear in a random order to ensure variety.
   - Type your answer and press Enter.
   - The system checks answers case-insensitively (e.g., "paris" and "Paris" 
     are both correct).
   - Immediate feedback (Correct/Incorrect) is provided after every question.

Step 5: Results
   - After finishing your questions, your score and percentage will be displayed.
   - You will be asked if another user wants to take the quiz.
     - Type 'yes' to let a new user play.
     - Type anything else (e.g., 'no') to finish the session.

Step 6: Overall Statistics
   - When the session ends, the application displays:
     1. The name and score of the highest-performing user.
     2. The average score of all users who played during the session.

6. TROUBLESHOOTING
------------------------------------------------------------------------------
Error: "ModuleNotFoundError: No module named 'quiz'"
   - Cause: You might be running the script from inside the 'quiz' folder 
     instead of the root folder.
   - Fix: Move up one directory to 'console_quiz_app' and run 'python main.py'.

Error: "Invalid input" when entering numbers
   - Cause: Entering text or special characters when a number is required.
   - Fix: Ensure you enter a whole integer (e.g., 5) for question counts.

==============================================================================