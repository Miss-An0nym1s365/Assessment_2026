import random

def equation_gen(question):
    """generates equations"""

# error = "Please enter a valid inter answer..."

num_choose = random.randint(1, 1000)
num_choose2 = random.randint(1, 1000)

math_expression = f"{num_choose} + {num_choose2} "

for item in range(0, 5):
    equation_gen = random.choice()

print(math_expression)


#
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