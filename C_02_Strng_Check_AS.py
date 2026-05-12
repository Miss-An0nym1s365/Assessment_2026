# Check that users have entered a valid
# option based on a list


def string_checker(question, valid_ans=("yes", "no")):

    error = f"Please enter a valid option from the following list: {valid_ans}"

    while True:

        # Get user response and amke sure it's lowercase
        user_response = input(question).lower()

        for item in valid_ans:
            # check if the user response is a word in the list

            if item == user_response:
                return item

            # check if the user response is the same as
            # the first letter of an item in the list
            elif user_response == item[0]:
                return item

        # print error if user does not enter something that is valid
        print(error)
        print()


# Main routine

mathtype_list = ["*", "+", "-", "xxx"]


want_instructions = string_checker("Do you want to see the instructions?")

print("You chose: ", want_instructions)

user_choice = string_checker("Choose equation type: ", mathtype_list)

if user_choice == "*":
    feedback = "You chose multiplication"
elif user_choice == "+":
    feedback = "You chose addition"
elif user_choice == "-":
    feedback = "You chose subtraction"
elif user_choice == "xxx":
    feedback = "You chose to exit the program."
else:
    print(error)

print("You chose: ", feedback)# Check that users have entered a valid
# option based on a list
def string_checker(question, valid_ans=("yes", "no")):


    while True:

        # Get user response and amke sure it's lowercase
        user_response = input(question).lower()

        for item in valid_ans:
            # check if the user response is a word in the list

            if item == user_response:
                return item

            # check if the user response is the same as
            # the first letter of an item in the list
            elif user_response == item[0]:
                return item

        # print error if user does not enter something that is valid
        print(error)
        print()
