class Bit:

  def __init__(self):
    self.bit = [0] * MAX

  def update(self, x, v):
    while x < MAX:
      self.bit[x] += v
      x += x & (-x)

  def query(self, x):
    res = 0
    while x > 0:
      res += self.bit[x]
      x -= x & (-x)
    return res

  def find_kth_index(self, k):
    low, high = 0, MAX - 1
    res = -1
    while low <= high:
      mid = (low + high) // 2
      now = self.query(mid)
      
      if now >= k:
        res = mid
        high = mid - 1
      else:
        low = mid + 1
    return res