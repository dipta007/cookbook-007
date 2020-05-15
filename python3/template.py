""" Python 3 compatibility tools. """
from __future__ import division, print_function
import itertools
import sys

if sys.version_info[0] < 3:
  input = raw_input
  range = xrange

  filter = itertools.ifilter
  map = itertools.imap
  zip = itertools.izip

input = sys.stdin.read().split('\n')[::-1].pop
out = __pypy__.builders.StringBuilder()


def give_it_all():
  if sys.version_info[0] < 3:
    os.write(1,out.build())
  else:
    os.write(1,out.build().encode())


# Built In GDC is much slower on python
def gcd(x, y):
  """ greatest common divisor of x and y """
  while y:
    x, y = y, x % y
  return x


def input1(type=int):
  return type(input())


def input2(type=int):
  [a, b] = list(map(type, input().split()))
  return a, b


def input3(type=int):
  [a, b, c] = list(map(type, input().split()))
  return a, b, c


def input_array(type=int):
  return list(map(type, input().split()))


def input_string():
  s = input()
  return list(s)


def main():
  pass

if __name__ == '__main__':
  main()