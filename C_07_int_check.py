def int_check(question, low=0, exit_code="xxx"):

    # Create the error message
    if low is None:
        error = "Please enter the number of questions you'd like to ."

    else:
        error = f"Please enter the number of questions you'd like to answer"

    while True:

        response = input(question).lower()

        # Check for infinite mode / exit code

        try:
            response = int(response)

            # Too low
            if low is not None and response < low:
                print(error)

            # Valid response
            else:
                return response

        except ValueError:
            print(error)


# Main routine starts here

# Ask user for number of rounds
num_questions = int_check(
    "How many rounds? <Press Enter for infinite mode>: ",
    low=1,
    exit_code="xxx"
)

# Check for infinite mode
if num_questions == "":
    mode = "infinite"
    num_questions = float("inf")

else:
    mode = "normal"

print()
print(f"Mode: {mode}")
print(f"Rounds: {num_questions}")