db = {
"Tryptophan": ["UGG"],
"Methionine": ["AUG"],
"Leucine": ["UUA", "UUG"],
"Tyrosine": ["UAU", "UAC"],
"Cysteine": ["UGU", "UGC"],
"STOP": ["UAA", "UAG", "UGA"],
"Phenylalanine": ["UUU", "UUC"],
"Serine": ["UCU", "UCC", "UCA", "UCG"]
}


def proteins(strand):
    return _analyze(_separate(strand))

def _separate(dna: str) -> list:
    result = []
    codon = ""
    for letter in dna:
        codon += letter
        if len(codon) == 3:
            result.append(codon)
            codon = ""
    return result

def _analyze(dna: list, db=db) -> None:
    result = []
    for codon in dna:
        for i, v in db.items():
            for j in v:
                if codon == j:
                    if i == "STOP":
                        return result
                    else:
                        result.append(i)
    return result
