from Bio import SeqIO

records = list(SeqIO.parse("rosalind_splc.txt", "fasta"))
table = {"UUU": "F", "UUC": "F", "UUA": "L", "UUG": "L",
         "UCU": "S", "UCC": "S", "UCA": "S", "UCG": "S",
         "UAU": "Y", "UAC": "Y", "UAA": "STOP", "UAG": "STOP",
         "UGU": "C", "UGC": "C", "UGA": "STOP", "UGG": "W",
         "CUU": "L", "CUC": "L", "CUA": "L", "CUG": "L",
         "CCU": "P", "CCC": "P", "CCA": "P", "CCG": "P",
         "CAU": "H", "CAC": "H", "CAA": "Q", "CAG": "Q",
         "CGU": "R", "CGC": "R", "CGA": "R", "CGG": "R",
         "AUU": "I", "AUC": "I", "AUA": "I", "AUG": "M",
         "ACU": "T", "ACC": "T", "ACA": "T", "ACG": "T",
         "AAU": "N", "AAC": "N", "AAA": "K", "AAG": "K",
         "AGU": "S", "AGC": "S", "AGA": "R", "AGG": "R",
         "GUU": "V", "GUC": "V", "GUA": "V", "GUG": "V",
         "GCU": "A", "GCC": "A", "GCA": "A", "GCG": "A",
         "GAU": "D", "GAC": "D", "GAA": "E", "GAG": "E",
         "GGU": "G", "GGC": "G", "GGA": "G", "GGG": "G", }



def splc(records):

    mainS = str(records[0].seq.transcribe())
    intr = [str(i.seq.transcribe()) for i in records[1:]]

    for i in intr:
        mainS = mainS.replace(i, '')


    P = ''
    if len(mainS) % 3 == 0:
        for i in range(0, len(mainS), 3):
            c = mainS[i:i + 3]
            if table[c] != 'STOP':
                P += table[c]

    return P


print(splc(records))