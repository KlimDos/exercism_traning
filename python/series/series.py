def slices(series: str, length: int):
    result = []
    series_len = len(series)
    if series == "" or length <= 0 or series_len < length:
        raise ValueError("Incorrect input")
    for i in range(series_len):
        substring = series[i:i+length]
        if len(substring) == length:
            result.append(substring)
    return result
