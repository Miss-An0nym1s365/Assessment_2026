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

Welcome to the ULTIMATE MATH QUIZ!

Choose:
- Addition (+)
- Subtraction (-)
- Multiplication (*)

You can:
- Press ENTER for infinite mode
- Type xxx to quit early

Try to answer as many questions correctly as possible!

Good luck 😎
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
    """Checks integer input"""

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

    num1 = random.randint(1, 20)
    num2 = random.randint(1, 20)

    if choice == "+":
        question = f"{num1} + {num2}"
        answer = num1 + num2

    elif choice == "-":
        question = f"{num1} - {num2}"
        answer = num1 - num2

    else:
        question = f"{num1} * {num2}"
        answer = num1 * num2

    return question, answer


def quiz_history(correct, wrong):
    """Displays quiz history"""

    total = correct + wrong

    if total == 0:
        print("No questions answered.")
        return

    correct_percent = correct / total * 100
    wrong_percent = wrong / total * 100

    print()
    print("📜 Quiz History 📜")
    print(f"Correct: {correct}")
    print(f"Wrong: {wrong}")
    print(f"Correct Percentage: {correct_percent:.1f}%")
    print(f"Wrong Percentage: {wrong_percent:.1f}%")


# Main routine starts here

print("✖️➕➖ Welcome to THE Math Quiz ➖➕✖️")
print()

# Instructions
want_instructions = yes_no("Do you want instructions? ")

if want_instructions == "yes":
    instructions()

# Choose math type
math_type = string_checker(
    "Choose equation type (+, -, *): ",
    ["+", "-", "*"]
)

# Number of questions
num_questions = int_check(
    "How many questions? <Press Enter for infinite mode>: ",
    low=1,
    exit_code="xxx"
)

# Quit program
if num_questions == "xxx":
    print("Program exited.")

else:

    # Infinite mode
    if num_questions == "":
        mode = "infinite"
        num_questions = float("inf")

    else:
        mode = "normal"

    print()
    print(f"Mode: {mode}")

    # Quiz variables
    rounds_played = 0
    correct_answers = 0
    wrong_answers = 0

    # Quiz loop
    while rounds_played < num_questions:

        rounds_played += 1

        print()
        print(f"Question {rounds_played}")

        # Generate question
        question, correct_answer = equation_generator(math_type)

        print(question)

        # Get answer
        user_answer = input("Your answer: ").lower()

        # Quit early
        if user_answer == "xxx":
            print("You exited the quiz early.")
            break

        # Check answer
        try:
            user_answer = int(user_answer)

            if user_answer == correct_answer:
                print("✅ Correct!")
                correct_answers += 1

            else:
                print("❌ Incorrect")
                print(f"The correct answer was {correct_answer}")
                wrong_answers += 1

        except ValueError:
            print("Please enter a whole number.")
            wrong_answers += 1

    # Quiz summary
    print()
    print("🎉 Quiz Finished 🎉")

    total_answered = correct_answers + wrong_answers

    if total_answered > 0:
        score_percent = correct_answers / total_answered * 100

        print(f"You got {correct_answers} correct.")
        print(f"You got {wrong_answers} wrong.")
        print(f"Your score was {score_percent:.1f}%")

    # Ask for history
    see_history = yes_no("Do you want to see your quiz history? ")

    if see_history == "yes":
        quiz_history(correct_answers, wrong_answers)

print()
print("Thanks for playing!")
