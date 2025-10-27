# -------------------------
def new_gmae():
    guesses = []
    correct_guesses = 0
    question_num = 1

    for key in question:
        print("-------------------------")
        print(key)
        for i in options[question_num-1]:
            print(i)

        #     question_num += 1
        guess = input("Enter (A, B, C, or D): ").upper()
        guesses.append(guess)

        check_answer(question.get(key), guess)

        correct_guesses += check_answer(question.get(key), guess)
        question_num += 1

    # display_score(guesses, correct_guesses, question)    pass

# -------------------------
def check_answer(answer,guess):
    if answer == guess:
        print("CORRECT!")
        return 1
    else:
        print("WRONG!")
        return 0

# -------------------------
def display_score():
    pass

# -------------------------
def play_again():
    pass


question = {
    "Who created Python?: ": "A",
    "What year was Python created?: ": "B",
    "Python is tributed to which comedy group?: ": "C",
    "Is the Earth round?: ": "A"
}

options = [["A. Guido van Rossum", "B. Elon Musk", "C. Bill Gates", "D. Mark Zuckerburg"],
           ["A. 1989", "B. 1991", "C. 2000", "D. 2016"],
           ["A. Lonely Island", "B. Smosh", "C. Monty Python", "D. SNL"],
           ["A. True", "B. False", "C. sometimes", "D. What's Earth?"]]

new_gmae()