import MapReduce
import sys
from collections import Counter

"""
The relationship "friend" is often symmetric, meaning that if I am your friend, 
you are my friend. Implement a MapReduce algorithm to check whether this property holds. 
Generate a list of all non-symmetric friend relationships.
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    # key: person id
    # value: all the friendship tuples where person participates
    mr.emit_intermediate(record[0], record[1])      
    mr.emit_intermediate(record[1], record[0])

def reducer(person_id, list_of_friendships):
    # Emits the missing symetric friendships
    friendship_count = Counter(list_of_friendships)
    for f_id, count in reversed(friendship_count.most_common()):
      if count == 1:
        mr.emit((person_id, f_id))
      else:
        break
    
# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
