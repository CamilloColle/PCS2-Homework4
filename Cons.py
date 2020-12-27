import Bio.Seq
from Bio.Seq import Seq
from Bio import SeqIO

records = list(SeqIO.parse("rosalind_cons.txt", "fasta"))

A = [0 for i in range(len(records[0].seq))]
T = [0 for i in range(len(records[0].seq))]
C = [0 for i in range(len(records[0].seq))]
G = [0 for i in range(len(records[0].seq))]
conseq = []

def cons():
    for i in records:
        for b in range(len(i.seq)):
            if i.seq[b] == 'A':
                A[b] += 1
            elif i.seq[b] == 'T':
                T[b] += 1
            elif i.seq[b] == 'C':
                C[b] += 1
            elif i.seq[b] == 'G':
                G[b] += 1

    for i in range(len(A)):
        d = {}
        d['A'] = A[i]
        d['T'] = T[i]
        d['C'] = C[i]
        d['G'] = G[i]
        M = max(d.values())
        for j in d:
            if d[j] == M:
                conseq.append(j)
                break


    print(''.join(conseq))
    print('A:',*A)
    print('C:',*C)
    print('G:',*G)
    print('T:',*T)




print(cons(), end='\n')