import MapReduce
import sys

"""
Inverted index. 
Given a set of documents, an inverted index is a dictionary where each word 
is associated with a list of the document identifiers in which that word appears. 
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    # key: document identifier
    # value: document contents
    key = record[0]
    value = record[1]
    words = value.split()
    words = set(words)
    for w in words:
      mr.emit_intermediate(w, key)

def reducer(key, list_of_documents):
    # key: word
    # value: list of document names
    mr.emit((key, list_of_documents))

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
