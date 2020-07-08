def is_valid(isbn):
    clean = ""
    isbn_pure = isbn[:len(isbn)-1]
    for i in isbn_pure:
        if i.isdigit():
            clean += i
    if len(clean) != 9:
        return False
    elif isbn[-1] == "X":
        result = 10
    elif isbn[-1].isdigit():
        result = int(isbn[-1])
    else:
        return False
    for j in range(2, 11):
        z = 10 - j
        result += int(clean[z]) * j
    
    return not bool(result % 11)
