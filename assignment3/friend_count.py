import MapReduce
import sys

"""
Consider a simple social network dataset consisting of key-value pairs where each key is a person 
and each value is a friend of that person. Describe a MapReduce algorithm to count 
the number of friends each person has.
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
	# record: 2 element list representing a frienship [f1, f2]
	# emits: (f1, 1)
    mr.emit_intermediate(record[0], 1)

def reducer(key, list_of_friends):
	# key: person id
	# value: list of friends
    mr.emit((key, len(list_of_friends)))

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
