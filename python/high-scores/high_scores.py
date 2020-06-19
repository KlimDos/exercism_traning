def latest(scores: list) -> int:
    result = list(reversed(scores))
    return result[0]

def personal_best(scores: list) -> int:
    result = sorted(scores, reverse=True)
    return result[0]

def personal_top_three(scores: list) -> list:
    result = sorted(scores, reverse=True)
    return result[:3]
