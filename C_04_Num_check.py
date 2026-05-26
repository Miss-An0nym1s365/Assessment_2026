def num_check(question, num_type=int, low=-1,high=2001, exit_code="xxx"):
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
                print(f"Error: enter a number higher than (or equal to) 0.")
            elif response >= high:
                print(f"Error: Please enter a number lower than (or equal to) 2000")
            else:
                return response

        # Show error if response is invalid
        except ValueError:
            print("Error: Please enter whole numbers only.")

# Main routine
number = num_check("Number: ")
print("You entered: ", number)