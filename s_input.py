def s_input(question: str, acceptable: list):
    """

    :rtype: object
    """
    accepted = False
    while not accepted:
        x = input(question)
        x = x.replace(" ", "").lower()
        for z in acceptable:
            if x == z:
                accepted = True
                return x
            if not accepted:
                print("hi")
