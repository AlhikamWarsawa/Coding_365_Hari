def grow(x):
    from functools import reduce
    return reduce(lambda acc, curr: acc * curr, x, 1)

print(grow([2,2,2,2,2,2]))