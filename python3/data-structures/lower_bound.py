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
