def ts() -> float: 
  loop = 100
  # print(fun(2.0))
  # return
  while loop > 0:
    loop -= 1

    m1 = ( low * 2.0 + high ) / 3.0
    m2 = ( low + high * 2.0) / 3.0
    y1 = fun(m1)
    y2 = fun(m2)

    # print(y1, y2)

    # big - small - big
    if y1 > y2:
      low = m1
    else:
      high = m2

    # small - big - small
    if y1 > y2:
      high = m2
    else:
      low = m1
  return (low + high) / 2.0

# Ternary Search on INTS
lo, hi = -1, n
while hi - lo > 1:
    mid = (hi + lo) >> 1
    if f(mid) > f(mid + 1):
      hi = mid
    else:
      lo = mid
# lo + 1 is the answer

# Ternary Search on ARRAY INT
def ternary_search(l, r, x) -> int:
  if r>=l:
    mid1 = l + (r-l) // 3
    mid2 = r -  (r-l) // 3
    if ar[mid1] == x:
      return mid1
    if ar[mid2] == x:
      return mid2
    if x<ar[mid1]:
      return ternary_search(l, mid1-1, x)
    elif x>ar[mid2]:
      return ternary_search(mid2+1, r, x)
    else:
      return ternary_search(mid1+1, mid2-1, x)
  return -1
