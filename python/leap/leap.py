def leap_year(year: int) -> bool:
    result = bool(
        not year % 4 and year % 100 or not year % 400
    )
    return result
