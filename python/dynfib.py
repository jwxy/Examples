#!/usr/bin/env python

fmap = [0, 1]

def fib(n):
    """
    Return the Fibonacci number for the given integer. Prior results are stored
    (fmap) to reduce recursion (dynamic programming).
    parameters:
      n - integer
    returns:
      Fibonacci number
    """
    global fmap
    if n >= len(fmap):
        fmap.append(fib(n - 1) + fib(n - 2))
    return fmap[n]

nums = [1, 2, 5, 10, 100]

print '   N  Fn'    
for n in nums:
    print '%4d: %d' % (n, fib(n))