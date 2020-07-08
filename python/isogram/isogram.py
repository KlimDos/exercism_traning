import string as s

def is_isogram(string: str) -> bool:
    clean = [x for x in string.lower() if x in s.ascii_lowercase]
    return bool(len(clean) == len(set(clean))), string

st = "Alphabet"

r = is_isogram(st)

print(r, st)