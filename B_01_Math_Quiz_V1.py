import random


# Functions go here
def yes_no(question):
    """Checks user response to a yes / no question"""

    while True:

        response = input(question).lower()

        if response == "yes" or response == "y":
            return "yes"

        elif response == "no" or response == "n":
            return "no"

        else:
            print("Please enter yes / no")


def instructions():
    """Displays instructions"""

    print("""
**** Instructions ****

Hello and Wellcome to the ULTIMATE MATH QUIZ!

To begin, you will choose the types of questions
you would like to answer. You can choose from:
- addition(+)
- subtraction(-)
- multiplication(*)

Then you must choose how many rounds you'd like to play.

You can exit the quiz anytime by typing "xxx"

Your end goal is to get as many a questions possible without
failing miserably. 

Do YOU have what it takes? 🫵🤨
""")


def string_checker(question, valid_ans):
    """Checks for valid response"""

    while True:

        response = input(question).lower()

        for item in valid_ans:

            if response == item:
                return item

            elif response == item[0]:
                return item

        print(f"Please choose from: {valid_ans}")
        print()


def int_check(question, low=None, exit_code=None):
    """Checks integer input for number of questions"""

    while True:

        response = input(question).lower()

        # Infinite mode
        if response == "":
            return ""

        # Exit code
        if response == exit_code:
            return exit_code

        try:
            response = int(response)

            if response < low:
                print(f"Please enter a number that is {low} or more.")

            else:
                return response

        except ValueError:
            print("Please enter a whole number.")


def equation_generator(choice):
    """Generates equations"""

    num_choose = random.randint(1, 20)
    num_choose2 = random.randint(1, 20)

    num_choose_x = random.randint(1, 12)
    num_choose_x2 = random.randint(1, 12)

    if choice == "+":
        question = f"{num_choose} + {num_choose2}"
        answer = num_choose + num_choose2

    elif choice == "-":
        question = f"{num_choose} - {num_choose2}"
        answer = num_choose - num_choose2

    else:
        question = f"{num_choose_x} x {num_choose_x2}"
        answer = num_choose_x * num_choose_x2

    return question, answer


# Main routine starts here

print("✖️➕➖ Welcome to THE Math Quiz ➖➕✖️")
print()

# Instructions
want_instructions = yes_no("Do you want instructions? ")

if want_instructions == "yes":
    instructions()

# Let user choose math type
math_type = string_checker(
    "Choose equation type (+, -, *): ",
    ["+", "-", "*"]
)

# Number of questions, user asks!!!!!!!!
num_questions = int_check(
    "How many questions? <Press Enter for infinite mode>: ",
    low=1,
    exit_code="xxx"
)

# Quit program/quiz
if num_questions == "xxx":
    print("You chose to exit early >:|")

else:

    # Infinite mode
    if num_questions == "":
        mode = "infinite"

    else:
        mode = "normal"

    print()
    print(f"{mode} chosen")

    # Quiz answers for users history and questions
    quiz_history = []
    correct_answers = 0
    wrong_answers = 0

    # Quiz loop
    while questions_answered < num_questions:

        questions_answered += 1

        print()
        print(f"Question {questions_answered}")

        # Generate question
        question, correct_answer = equation_generator(math_type)

        print(question)

        # Get the user's answer
        user_answer = input("Your answer: ").lower()

        # Let the user quit the quiz early
        if user_answer == "xxx":
            print("You exited the quiz.")
            break

        # Check the user's answer
        try:
            user_answer = int(user_answer)

            if user_answer == correct_answer:
                print("✅ Correct-a-mundo!")
                correct_answers += 1

            else:
                print("❌ Incorrect...")
                print(f"The correct answer was {correct_answer}")
                wrong_answers += 1

        except ValueError:
            print("Please enter a whole number, try again.")

    # Quiz summary/ history for user
    print()
    print("🎉 Quiz Finished 🎉")

    quiz_history.append(
        f"{question[0]} Your answer: {user_response} | The Correct answer: {question[1]}")

    # Quiz history
    quiz_history = yes_no("Do you wanna see your quiz history? (￣▽￣)")

    if quiz_history == "yes":
        print("Quiz History")
        for item in quiz_history:
            print(item)
        print()
        print(f"Total Correct: {correct_answers}")
        print(f"Total Incorrect: {wrong_answers}")
        print()

        # Output stats
        print(
            f" Correct Answers: {correct_answers / num_questions * 100: .2f}% | Incorrect answers: {wrong_answers / num_questions * 100: .2f}%")

        print()
        print("Thanks for playing!")
        print("You are now a smarter person! :)")