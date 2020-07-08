def square_of_sum(number: int):
    result = 0
    for i in range(1, number + 1):
        result += i
    result = result ** 2
    return result


def sum_of_squares(number):
    result = 0
    for i in range(1, number + 1):
        result += i ** 2
    return result


def difference_of_squares(number):
    result = square_of_sum(number) - sum_of_squares(number)
    return result
