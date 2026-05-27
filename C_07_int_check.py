def int_check(question, low=None, exit_code=None):

    while True:

        response = input(question).lower()

        # Infinite mode
        if response == "":
            return ""

        # Exit program
        if response == exit_code:
            return exit_code

        try:
            response = int(response)

            # Check number is high enough
            if response < low:
                print(f"Please enter a number that is {low} or more.")

            else:
                return response

        except ValueError:
            print("Please enter the number of questions you'd like to be asked")


# Main routine starts here

num_questions = int_check(
    "How many questions? <Press Enter for infinite mode>: ",
    low=1,
    exit_code="xxx"
)

# Check for infinite mode
if num_questions == "":
    mode = "infinite"
    print("You chose infinite mode")

# Check for quit
elif num_questions == "xxx":
    print("You chose to exit the program early >:|")

# Normal mode
else:
    mode = "normal"
    print(f"You're going to be asked {num_questions} questions.")