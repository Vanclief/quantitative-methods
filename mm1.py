import math

def calc_ls(lamda, mu):
    return lamda / (mu - lamda) # lambda typo on purpose

def calc_ws(lamda, mu):
    return (1 / (mu - lamda)) # lambda typo on purpose

def calc_lq(lamda, mu):
    return (lamda * lamda) / mu * (mu - lamda) # lambda typo on purpose

def calc_wq(lamda, mu):
    return lamda / mu * (mu - lamda) # lambda typo on purpose

def calc_pn(p, n):
    return (1 - p) * math.pow(p, n)

def calc_pls(p, n):
    return math.pow(p, (n + 1))

def calc_pws(p, u, t):
    e = math.exp(1)
    neg_u = u * -1
    power = neg_u * (1-p) * t
    return math.pow(e, power)

def calc_pwq(p, u, t):
    e = math.exp(1)
    neg_u = u * -1
    power = neg_u * (1-p) * t
    return math.pow((p * e), power)


def main():
    print("he")

if __name__ == "__main__":
    main()
