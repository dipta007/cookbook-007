def factorialDigitExtended(n, base):
  res = 0.0
  for i in range(1, n+1):
    res += math.log10(i) / math.log10(base)
  return int(res) + 1