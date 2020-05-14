MAX_N = 1000004
marked = []
primes = []

def is_prime(n):
  if n < 2:
    return False
  if n == 2:
    return True
  if n%2 == 0:
    return False
  return marked[n] == 0


def sieve(n):
  global marked
  marked = [0 for _ in range(MAX_N)]
  primes.append(2)

  sq = int(math.sqrt(n))
  for i in range(3, sq+1, 2):
    if marked[i] == 0:
      primes.append(i)
      for j in range(i*i, n+1, i + i):
        marked[j] = 1