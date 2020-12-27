from Bio import SeqIO

rec = sorted([str(i.seq) for i in SeqIO.parse("rosalind_lcsm.txt", "fasta")], key = len)

def lcsm():
    s = ''
    m = rec[0]
    rec1 = rec[1:]
    for i in range(len(m)):
        for j in range(1, len(m)):
            match = False
            sub = m[i:j+1]
            for k in rec1:
                if sub in k:
                    match = True
                else:
                    break

            if match==True and len(sub) > len(s):
                s = sub

    return s


print(lcsm())