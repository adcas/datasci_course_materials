import MapReduce
import sys

"""
Assume you have two matrices A and B in a sparse matrix format, where each record is of the form i, j, value.
Design a MapReduce algorithm to compute matrix multiplication: A x B
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

ROWS_A, COLS_B = 5, 5

def mapper(record):
    # record: [matrix, i, j, value]
    # emits: result matrix index and row value

    [matrix, i, j, value] = record
    key = {}
    if matrix == 'a':
      key = str(i) + ' %s' 
      moving_index = COLS_B
      static_index = j
    else:
      key = '%s ' + str(j)
      moving_index = ROWS_A
      static_index = i

    for p in xrange(moving_index):
      key_p = key % str(p)
      mr.emit_intermediate(key_p, (matrix , static_index, value))

def reducer(key, list_of_values):
    # key: position in result matrix
    # value: list of values from input matrixs to compute result
    total = 0
    m_a = {}
    m_b = {}
    for v in list_of_values:
      m = m_a if v[0] == 'a' else m_b
      m[v[1]] = v[2]

    m_small, m_big = (m_a, m_b) if len(m_a) < len(m_b) else (m_b, m_a)
    for i, v in m_small.iteritems():
      total += (v*m_big.get(i, 0))

    i, j = key.split()
    mr.emit((int(i), int(j), total))

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
