def num_check(question, num_type=int, low=0,high=2000, exit_code="xxx"):
    """checks the user responses are valid"""

    while True:
        # Ask user question and return response if
        # exit code is entered
        response = input(question)
        if response == exit_code:
            return response

        # Check response is more than the minimum
        try:
            response = num_type(response)

            if response <= low:
                print("Error: enter a number more than {low}.")
            else:
                return response

        # Show error if response is invalid
        except ValueError:
            print("Error: Please enter numbers only.")

# Main routine
number = num_check("Number: ")
print("You entered: ", number)
