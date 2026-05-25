import random

def equation_gen(question):
    """generates equations"""

# error = "Please enter a valid inter answer..."
while True:
    num_choose = random.randint(1, 1000)
    num_choose2 = random.randint(1, 1000)

    math_expression = f"{num_choose} + {num_choose2} "

    print(math_expression)

    again = input("Press <enter> to generate another equation: ")

    if again == "xxx":
        print()
        print("Program continues...")
        break


# math_answer = eval(math_expression)
#
# # print(f"The answer is {math_answer}")
#
# while True:
#
#     user_response = input(math_expression)
#
#     if user_response == math_answer:
#         print("HOORAY! You got it correct 🙌")
#     elif user_response == "xxx":
#         print("You chose to exit the program")
#     elif user_response != math_answer:
#         print(f"Sorry, the answer was actually {math_answer}")
#     else:
#         print(error)
# # main routine
#
#     print("end of question")