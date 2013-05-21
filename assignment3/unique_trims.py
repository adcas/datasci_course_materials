import MapReduce
import sys

"""
Consider a set of key-value pairs where each key is sequence id and each value 
is a string of nucleotides, e.g., GCTTCCGAAATGCTCGAA....
Write a MapReduce query to remove the last 10 characters from each string of nucleotides, 
then remove any duplicates generated.
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

CHARS_TO_REMOVE = 10

def mapper(record):
    nucleotides = record[1]
    mr.emit_intermediate(nucleotides[:-CHARS_TO_REMOVE], 1)

def reducer(key, list_of_values):
    mr.emit(key)

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
