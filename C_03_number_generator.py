import random

def math_ans(question):
    """users see if their answers are right"""

num_choose = random.randint(1, 1000)

user_response = []

check_ans = num_choose + num_choose

while True:
    if user_response == check_ans:
        print("HOORAY! you got it correct :)")
    elif user_response != check_ans:
        print(f"The answer was actually {check_ans}")
    elif user_response == "xxx":
        print("You chose to exit the program")
    else:
        error = "Please enter a valid integer answer..."

# main routine

give_ans = math_ans(f"What is {num_choose} + {num_choose} = ")