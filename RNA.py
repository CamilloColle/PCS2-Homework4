with open("rosalind_rna.txt") as f:
    s = str(f.readline())


def rna(s):
    dna = []
    for i in s:
        if i == 'A':
            dna.append('A')
        elif i == 'T':
            dna.append('U')
        elif i == 'C':
            dna.append('C')
        elif i == 'G':
            dna.append('G')

    return ''.join(dna)


print(rna(s))