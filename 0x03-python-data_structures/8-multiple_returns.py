def multiple_returns(sentence):
    for i in range(len(sentence)):
        for x in sentence[0]:
            multiple_return = (i, x)
        return multiple_return
