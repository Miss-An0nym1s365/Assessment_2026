import random

def equation(question):
    """generates equations"""

error = "Please enter a valid inter answer..."

num_choose = random.randint(1, 1000)
num_choose2 = random.randint(1, 1000)

math_expression = f"{num_choose} + {num_choose2} "

question = math_expression

# print(math_expression)

math_answer = eval(question)

# print(f"The answer is {math_answer}")

while True:

    user_response = input(question)

    if user_response == math_answer:
        print("HOORAY! You got it correct 🙌")
    elif user_response != math_answer:
        print(f"Sorry, the answer was actually {math_answer}")
    elif user_response == "xxx":
        print("You chose to exit the program")
    else:
        print(error)
# main routine
