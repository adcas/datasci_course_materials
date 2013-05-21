import MapReduce
import sys
from itertools import groupby
from collections import defaultdict

"""
Relational join as a MapReduce query
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

FIRST_TABLE = 'order'
SECOND_TABLE = 'line_item'

def mapper(record):
    mr.emit_intermediate(record[1], record)

def reducer(key, list_of_rows):
    # Group rows in tables
    list_of_rows.sort(key=lambda r: r[0])
    rows = defaultdict(list)
    for k, g in groupby(list_of_rows, lambda r: r[0]):
      rows[k] += g

    # Emit every joined row
    for r1 in rows[FIRST_TABLE]:
      for r2 in rows[SECOND_TABLE]:
        mr.emit(sum([r1, r2], []))
    

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
