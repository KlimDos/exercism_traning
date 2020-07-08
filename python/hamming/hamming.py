def distance(strand_a: str, strand_b: str) -> int:
    if len(strand_a) != len(strand_b):
        raise ValueError("strands should have the same length")
    return sum(1 for i in enumerate(strand_a) if strand_a[i[0]] != strand_b[i[0]])
