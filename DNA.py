with open("rosalind_dna.txt") as f:
    s = str(f.readline())


def dna(s):
    a = t = c = g = 0
    for i in s:
        if i == 'A':
            a += 1
        elif i == 'T':
            t += 1
        elif i == 'C':
            c += 1
        elif i == 'G':
            g += 1

    return[a, c, g, t]


print(*dna(s))