def latest(scores):
    size = len(scores)
    scores = scores[size-1]
    return(scores)

def personal_best(scores):
    scores = max(scores)
    return(scores)

def personal_top_three(scores):
    scores.sort(reverse = True)
    scores = scores[0:3]
    return(scores)
