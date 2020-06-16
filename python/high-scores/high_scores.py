# Please explain why I cant apply method list.reverse()
# just directry in return: {return scores.reverse()}

def latest(scores: list) -> int:
    scores.reverse()
    return scores[0]

def personal_best(scores: list) -> int:
    scores.sort(reverse=True)
    return scores[0]

def personal_top_three(scores: list) -> list:
    scores.sort()
    while len(scores) > 3:
        scores.pop(0)
    scores.reverse()
    return scores
