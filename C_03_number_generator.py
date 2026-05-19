import random

def user_response(question):
    """generates numbers for equations and stuff"""
    print(question)

    error = "Please enter a valid integer answer..."

    question = f"What is {num_choose} + {num_choose} = "

num_choose = random.randint(1, 1000)

check_ans = num_choose + num_choose

if user_response == check_ans:
    print("HOORAY! you got it correct :)")
elif user_response != check_ans:
    print(f"The answer was actually {check_ans}")
elif user_response == "xxx":
    print("You chose to exit the program")
else:
    print(error)