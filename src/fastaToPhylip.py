from Bio import SeqIO
import os
pathI = os.path.abspath("../data/testAlign.fasta")
pathO = os.path.abspath("../data/testAlign.phylip")
records = SeqIO.parse(pathI, "fasta")
count = SeqIO.write(records, pathO, "phylip")
print("Converted %i records" % count)
