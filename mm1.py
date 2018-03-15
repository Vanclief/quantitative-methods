import math
import os
import sys

# Fórmulas generales

def general():
    print('he')

# Fórmulas para M/M/1

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

def mm1():
    print('he')

# Fórmulas para el modelo M/M/S

def mms_p0(lamda, mu, s, p):
    suma = 0
    i = 0
    b = pow(lamda/mu, s) / (math.factorial(s) * (1-p))
    while(i < s):
        a = pow(lamda/mu, i) / math.factorial(i)
        suma += a
        i += 1
    suma += b
    return 1 / suma

def mms_lq(lamda, mu, s, p0, p):
    a = pow(lamda/mu, s) * p0 * p
    b = math.factorial(s) * pow(1-p, 2)
    return a/b

def mms_wq(lq, lamda):
    return lq / lamda

def mms_ws(wq, mu):
    return wq + (1/mu)

def mms_ls(lamda, ws):
    return lamda * ws

def mms_p_lt_s(lamda, mu, n, p0):
    a = pow(lamda/mu, n) * p0
    return a / math.factorial(n)

def mms_p_gt_s(lamda, mu, n, p0, s):
    a = pow(lamda/mu, n) * p0
    b = math.factorial(s) * pow(s, n-s)
    return a / b

def mms():
    lamda = int(input("Escribe el valor de Lambda: "))
    mu = int(input("Escribe el valor de mu: "))
    s = int(input("Escribe el valor de s (número de servidores): "))
    p = lamda / (s*mu)
    p0 = mms_p0(lamda, mu, s, p)
    lq = mms_lq(lamda, mu, s, p0, p)
    wq = mms_wq(lq, lamda)
    ws = mms_ws(wq, mu)
    ls = mms_ls(lamda, ws)
    print("P0 = ", p0)
    print("Lq = ", lq)
    print("Wq = ", wq)
    print("Ws = ", ws)
    print("Ls = ", ls)

    more = 1
    while more != 2:
        more = int(input("Calcular probabilidad? Si = 1, No = 2  >> "))
        if more == 1:
            n = int(input("Éscribe el número de servidores: "))
            if n > s:
                print(mms_p_gt_s(lamda, mu, n, p0, s))
            else:
                print(mms_p_lt_s(lamda, mu, n, p0))

    input("Presiona [Enter] para continuar...")

models = [
    {   "name" : "Fórmulas generales",
        "function" : general},
    {   "name" : "Modelo M/M/1",
        "function" : mm1},
    {   "name" : "Modelo M/M/S",
        "function" : mms},
    {   "name" : "Exit", "function" : exit}]

def main():
    while True:
        os.system('clear')

        for i, function in enumerate(models):
            for key, value in function.items():
                if key == 'name':
                    print(i, value)

        selection = input(">> ")

        try:
            if int(selection) < 0 : raise ValueError
            models[int(selection)]['function']()
        except (ValueError, IndexError):
            pass

if __name__ == "__main__":
    main()
