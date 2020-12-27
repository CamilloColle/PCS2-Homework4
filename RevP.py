from Bio.Seq import *
from Bio import SeqIO

records = list(SeqIO.parse("rosalind_revp.txt", "fasta"))
S = records[0].seq


for i in range(len(S)):
    for j in range(4, 13):
        if S[i:i+j]==reverse_complement(S[i:i+j]) and i+j <= len(S):
            print(i+1, j)
