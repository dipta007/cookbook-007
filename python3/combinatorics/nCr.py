# ncr dp
MX = 1004
ncr = [[0 for _ in range(MX)] for _in range(MX)]
ncr[0][0] = 1
lim_r = MX-2
for i in range(1, lim_r+1):
  for j in range(lim_r+1):
    if j > i:
      ncr[i][j] = 0
    elif j == i or j == 0:
      ncr[i][j] = 1
    else:
      ncr[i][j] = ncr[i-1][j-1] + ncr[i-1][j]

# nCr avoiding overflow
def ncr(n, m):
  ans, cur = 1, 2
  for i in range(m+1, n):
    ans *= i
    if cur <= n-m and ans % cur == 0:
      ans /= cur
      cur += 1
  return ans

# Use this if you need nCr too much in every tc
MAX 1000005
MOD 1000000007

fact = [0 for _ in range(MAX)]
inv = [0 for _ in range(MAX)]

def bigmod(b, p, m):
  res = 1 % m
  x = b % m
  while p:
    if p % 2 == 1:
      res = ( res * x ) % m
    x = ( x * x ) % m
    p = p // 2
  return res

# m MUST BE prime, Fermats theorem
def mod_inv(a, m):
  return bigmod(a, m-2, m)

def generate(n, m):
  fact[0] = 1
  for i in range(1, n):
    fact[i] = (i * fact[i - 1]) % m;
  
  inv[n - 1] = mod_inv(fact[n-1], m)
  for i in range(n-2, -1, -1):
    inv[i] = (inv[i + 1] * (i + 1)) % m

def nCr(n, r, mod):
  if r > n:
    return 0

  global fact, inv
  return (((fact[n] * inv[r]) % mod) * inv[n-r])%mod


# Permutation
MAX = 1004
npk = [[0 for _ in range(MAX)] for _ in range(MAX)]
def nPk():
  for i in range(MAX):
    for j in range(i+1):
      if not j:
        npk[i][j] = 1
      else:
        npk[i][j] = (npk[i][j-1] * (i-j+1)) % MOD
