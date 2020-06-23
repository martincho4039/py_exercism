def distance(strand_a, strand_b):
    if strand_a == strand_b:
        hamming_distance = 0
    elif strand_a.isalpha() == 0 or strand_b.isalpha() == 0:
        raise ValueError("Strings must contain only letters")
    elif len(strand_a) != len(strand_b):
        raise ValueError("Strings are not of the same length")
    else:
        hamming_distance = sum(a!=b for a, b in zip(strand_a, strand_b))
    return(hamming_distance)
