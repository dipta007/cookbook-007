class SegTree:
  def __init__(self, node, b, e):
    self._MX = 100004
    self._tree[self._MX * 3]
    self.init()

  def init(self, node, b, e):
    if b == e:
      self._tree[node] = arr[b]
      return
    
    left = node * 2
    right = left + 1
    mid = (b + e) // 2
    self.init(left, b, mid)
    self.init(right, mid+1, e)
    self._tree[node] = self._tree[left] + self._tree[right]
  
  def query(self, node, b, e, i, j):
    """We are on b - e interval, need the sum from i - j"""
    if i > e or j < b:
      return 0
    if b >= i and e <= j:
      return self._tree[node]

    left = node * 2
    right = left + 1
    mid = (b + e) // 2

    p1 = self.query(left, b, mid, i, j)
    p2 = self.query(right, mid+1, e, i, j)
    return p1 + p2

  def update(self, node, b, e, i, new_val):
    """We are on b - e interval, need to update ith index with new_val"""
    if i > e or i < b:
      return
    if b >= i and e <= i:
      self._tree[node] = new_val
      return
    
    left = node * 2
    right = left + 1
    mid = (b+e) // 2

    self.update(left, b, mid, i, new_val)
    self.update(right, mid + 1, e, i, new_val)
    self._tree[node] = self._tree[left] + self._tree[right]
  
