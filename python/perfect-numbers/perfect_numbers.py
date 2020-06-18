def classify(number: int) -> str:
    factors_sum = 0
    if number <= 0:
        raise ValueError(f"{number} not a natural number")
    for i in range(1, number):
        if number % i == 0:
            factors_sum += i
    if factors_sum == number:
        return "perfect"
    elif factors_sum > number:
        return "abundant"
    elif factors_sum < number:
        return "deficient"
