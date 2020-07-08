def find_anagrams(word: str, candidates: list) -> list:
    return [x for x in candidates if sorted(x.lower()) == \
        sorted(word.lower()) and word.lower() != x.lower()]
