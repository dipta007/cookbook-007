from types import GeneratorType

def bootstrap(f, stack=[]):
  def wrappedfunc(*args, **kwargs):
    to = f(*args, **kwargs)
    if stack:
      return to
    else:
      while True:
        if type(to) is GeneratorType:
          stack.append(to)
          to = next(to)
        else:
          stack.pop()
          if not stack:
            return to
          to = stack[-1].send(to)
  return wrappedfunc


@bootstrap
def dfs1(u, p):
  res = 0
  if u in adj:
    for v in adj[u]:
      if v != p:
        tmp = yield dfs1(v, u)
        res += tmp
        
  yield res