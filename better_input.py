def better_input(question: str, correct_answers: list, accepted=None):
    correct = False
    # loop until answer is within the correct_answers list
    while not correct:
        x = input(question)
        x = x.replace(" ", "").lower() # remove spaces and convert to lowercase
        for z in correct_answers:
            if x == z:
                # check answer against every possible answer
                accepted = True
                return x
                # return the answer as a string
        if not accepted:
            print("Invalid Option")

