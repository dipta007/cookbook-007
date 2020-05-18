# Input only the numbers nothing else, just like cin, a number once
file = 0
ii = 0
_inp = b''
def getchar():
  global ii, _inp
  if ii >= len(_inp):
    _inp = os.read(file, 100000)
    gc.collect()
    ii = 0
  if not _inp:
    return b' '[0]
  ii += 1
  return _inp[ii - 1]

def input_int():
  c = getchar()
  if c == b'-'[0]:
    x = 0
    sign = 1
  else:
    x = c - b'0'[0]
    sign = 0
  c = getchar()
  while c >= b'0'[0]:
    x = 10 * x + c - b'0'[0]
    c = getchar()
  if c == b'\r'[0]:
    getchar()
  return -x if sign else x
# Input Region