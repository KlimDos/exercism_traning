db = {
    "Tryptophan":       ["UGG"],
    "Methionine":       ["AUG"],
    "Leucine":          ["UUA", "UUG"],
    "Tyrosine":         ["UAU", "UAC"],
    "Cysteine":         ["UGU", "UGC"],
    "Phenylalanine":    ["UUU", "UUC"],
    "STOP":             ["UAA", "UAG", "UGA"],
    "Serine":           ["UCU", "UCC", "UCA", "UCG"]
}


def proteins(strand: str, db=db) -> list:
    result = []
    codon = ""
    for letter in strand:
        codon += letter
        if len(codon) == 3:
            for i, v in db.items():
                for j in v:
                    if codon == j:
                        if i == "STOP":
                            return result
                        else:
                            result.append(i)
            codon = ""
    return result
