def solve(numheads, numlegs):
    r = (numlegs - 2*numheads)//2
    c = (4*numheads - numlegs)//2
    return c, r
print(solve(35, 94))
