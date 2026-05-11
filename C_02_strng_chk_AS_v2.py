# this will be based on lists and will answer mathtype/ yes and no questions

def string_checker(question, valid_ans=("yes", "no")):

    error = f"Please enter a valid answer from the following list: {valid_ans}"

    while True:


        # make sure lowercase letters count
        user_respond = input(question).lower()

        for item in valid_ans:

            if item == user_respond:
                return item

            elif user_response == item[0]:
                return item

            print(error)
            print()

# Main Routine

mathtype_list = ["*", "+","-", "xxx"]

user_respond = string_checker("Choose equation type: ", mathtype_list)

if user_respond == "*":
    print("You have chosen multiplication...")
elif user_respond == "+":
    print("You have chosen addition...")
elif user_respond == "-":
    print("You have chosen subtraction...")
else:
    print("You have chosen to exit the program early, are you sure?")