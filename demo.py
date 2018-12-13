import pandas as pd
from genomics import Sequence, SequenceSet

sequences = DNASet.from_db("seq_list.csv", keys_from_file=True, tabular_file=True)
sequences.save_as("sequences.fna")
