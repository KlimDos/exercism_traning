def is_armstrong_number(number: int) -> bool:
    string = str(number)
    length = len(string)
    result = 0
    for i in str(number):
        result += int(i) ** length
    return bool(result == number)
