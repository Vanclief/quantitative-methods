import math

def mcm(seed):
   ans = math.pow(seed, 2)
   return ans

def formula(m, a, c, z):
    ans = ((a*z+c) % m)
    return ans, ans / m


z, result = formula(15, 12, 0, 7)
print(z, result)

