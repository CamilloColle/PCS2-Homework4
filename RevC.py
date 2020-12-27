with open("rosalind_revc.txt") as f:
    s = str(f.readline())


def revc(s):
    rev = []
    for i in s:
        if i == 'A':
            rev.insert(0,'T')
        elif i == 'T':
            rev.insert(0,'A')
        elif i == 'C':
            rev.insert(0,'G')
        elif i == 'G':
            rev.insert(0,'C')

    return ''.join(rev)


print(revc(s))