# functions go here

def yes_no(question):
    """Checks user response to a question is yes / no (y/n), returns 'yes' or 'no' """

    while True:

        response = input(question).lower()

        # check the user says yes / no / y /
        if response =="yes" or response == "y":
            return "yes"
        elif response == "no" or response == "n":
            return "no"
        else:
            print("please enter yes / no")


def instructions():
    """Prints instructions"""

    print("""
*** Instructions ****

Hello and Wellcome to the ULTIMATE MATH QUIZ.
To begin, you will choose what types of questions
you would like to answer. You can choose from addition,
subtraction or multiplication.

Then you must choose how many rounds you'd like to play.

Your end goal is to get as many a questions possible without
failing miserably. 

Do YOU have what it takes? 🫵🤨

    """)


# Main routine
print()
print("✖️➕➖➗Welcome to THE Math Quiz➗➖➕✖️")
print()

# ask the user if they want instructions (check they say yes / no)
want_instructions = yes_no("Do you want to see the instructions? ")

#Display the instructions if the user wants to see them...
if want_instructions == "yes":
    instructions()

print()
print("Program continues")