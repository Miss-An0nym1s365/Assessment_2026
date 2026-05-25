import random
def answer_check(user_answer, correct_answer):
    """Checks if the user's answer is correct"""

    if user_answer == correct_answer:
        print("Correct!")
    else:
        print("Incorrect!")
        print("The correct answer was", correct_answer)

while True:

    num_choose = random.randint(1, 1000)
    num_choose2 = random.randint(1, 1000)

    math_expression = f"{num_choose} + {num_choose2}"

    print()
    print(math_expression)

    correct_answer = num_choose + num_choose2

    user_answer = int(input("Your answer: "))

    answer_check(user_answer, correct_answer)

    again = input("Press <enter> to continue or 'xxx' to quit: ")

    if again == "xxx":
        print()
        print("Program continues...")
        break
