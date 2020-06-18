import string

def is_pangram(sentence: str) -> bool:
    abc = string.ascii_lowercase
    for letter in sentence:
        if letter.isalpha():
            abc = abc.replace(letter.lower(), "")
    return bool(abc == "")
