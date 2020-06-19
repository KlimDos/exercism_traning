db = {
    "G": "C",
    "C": "G",
    "T": "A",
    "A": "U"
}


# def to_rna(dna_strand: str, db=db) -> str:
#     orig = dna_strand
#     result = ""
#     for letter in orig:
#         flag = False
#         for k, v in db.items():
#             if letter == k:
#                 result += v
#                 flag = True
#         if not flag:
#             result += letter
#         flag = False
#     return result

def to_rna(dna_strand, db=db):
    ret = ''

    for char in dna_strand:
    	ret += db[char]

    return ret

s = "SDDDU"
print(to_rna(s))