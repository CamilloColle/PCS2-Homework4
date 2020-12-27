import Bio.Seq
from Bio.Seq import Seq
from Bio import SeqIO
record_dict = {}
records = list(SeqIO.parse("rosalind_gc.txt", "fasta"))


def gc():
    d = {}
    for item in records:
        count = item.seq.count('G') + item.seq.count('C')
        ratio = count/len(item.seq)*100
        d[item.id] = ratio
    M = max(d.values())
    for i in d:
        if d[i] == M:
            print(i)
            print(d[i])


gc()
