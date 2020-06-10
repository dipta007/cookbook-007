#Given a list of numbers of length n, this routine extracts a
#longest increasing subsequence.
#
#Running time: O(n log n)
#
#  INPUT: a vector of integers
#  OUTPUT: a vector containing the longest increasing subsequence

def lower_bound(nums, target):
    l, r = 0, len(nums) - 1
    res = len(nums)
    while l <= r:
        mid = int(l + (r - l) / 2)
        if nums[mid] >= target:
            res = mid
            r = mid - 1
        else:
            l = mid + 1
    return res
    
    
def upper_bound(nums, target):
    l, r = 0, len(nums) - 1
    res = len(nums)
    while l <= r:
        mid = int(l + (r - l) / 2)
        if nums[mid] > target:
            r = mid - 1
            res = mid
        else:
            l = mid + 1
    return res

def LIS(v, STRICTLY_INCREASING = False):
  best = []
  dad = [-1 for _ in range(len(v))]

  for i in range(len(v)):
    if STRICTLY_INCREASING:
      item = (v[i], 0)
      pos = lower_bound(best, item)
      item.second = i
    else:
      item = (v[i], i)
      pos = upper_bound(best, item)

    if pos == len(best):
      dad[i] = -1 if len(best) == 0 else best[-1][1]
      best.append(item)
    else:
      dad[i] = -1 if pos == 0 else best[pos-1][1]
      best[pos] = item

  ret = []
  i = best[-1][1]
  while i >= 0:
    ret.append(v[i])
    i = dad[i]

  return ret