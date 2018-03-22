import math
import os
import sys

# Fórmulas generales

def general():
    print("\nLey de Little:\nLs = Lambda * Ws\nLq = Lambda * Wq")
    print("Ws = Wq + 1/mu\nLs = Lq + lambda/mu\n\n")
    case = int(input("1. Lambda, Mu y Ws\n2. Lambda, Mu y Wq\n3. Lambda, Mu y Lq\n>> "))
    if case == 1:
        lamda = float(input("Escribe el valor de Lambda: "))
        mu = float(input("Escribe el valor de mu: "))
        ws = float(input("Escribe el valor Ws: "))
        ls = lamda * ws
        wq = ws - (1/mu)
        lq = lamda * wq
    elif case == 2:
        lamda = float(input("Escribe el valor de Lambda: "))
        mu = float(input("Escribe el valor de mu: "))
        wq = float(input("Escribe el valor Wq: "))
        lq = lamda * wq
        ws = wq + (1/mu)
        ls = lamda * ws
    elif case == 3:
        lamda = float(input("Escribe el valor de Lambda: "))
        mu = float(input("Escribe el valor de mu: "))
        lq = float(input("Escribe el valor Lq: "))
        ls = lq + (lamda/mu)
        wq = lq/lamda
        ws = wq + (1/mu)

    print("Lq = ", lq)
    print("Wq = ", wq)
    print("Ws = ", ws)
    print("Ls = ", ls)

    input("Presiona [Enter] para continuar...")

# Fórmulas para M/M/1

def mm1_ls(lamda, mu):
    return lamda / (mu - lamda) # lambda typo on purpose

def mm1_ws(lamda, mu):
    return (1 / (mu - lamda)) # lambda typo on purpose

def mm1_lq(lamda, mu):
    return (lamda * lamda) / (mu * (mu - lamda)) # lambda typo on purpose

def mm1_wq(lamda, mu):
    return lamda / (mu * (mu - lamda)) # lambda typo on purpose

def mm1_pn(p, u):
    print("P(n) = (1-p)p^n")
    n = float(input("Escribe el valor de n: "))
    return (1 - p) * math.pow(p, n)

def mm1_pls(p, u):
    print("P(Ls > n) = p^(n+1)")
    n = float(input("Escribe el valor de n: "))
    return math.pow(p, (n + 1))

def mm1_pws(p, u):
    print("P(Ws > t) = e^(-mu (1-p) t)")
    t = float(input("Escribe el valor de t: "))
    e = math.exp(1)
    neg_u = u * -1
    power = neg_u * (1-p) * t
    return math.pow(e, power)

def mm1_pwq(p, u):
    print("P(Wq > t) = pe^(-mu (1-p) t)")
    t = float(input("Escribe el valor de t: "))
    e = math.exp(1)
    neg_u = u * -1
    power = neg_u * (1-p) * t
    return p * math.pow(e, power)

mm1_probs = [
    {   "name" : "Pn",
        "function" : mm1_pn},
    {   "name" : "P(Ls > n)",
        "function" : mm1_pls},
    {   "name" : "P(Ws > t)",
        "function" : mm1_pws},
    {   "name" : "P(Wq > t)",
        "function" : mm1_pwq}]

def mm1():
    lamda = float(input("Escribe el valor de Lambda: "))
    mu = float(input("Escribe el valor de mu: "))
    s = float(input("Escribe el valor de s (número de servidores): "))
    p = lamda/(s*mu)
    ls = mm1_ls(lamda, mu)
    lq = mm1_lq(lamda, mu)
    ws = mm1_ws(lamda, mu)
    wq = mm1_wq(lamda, mu)
    print("p (factor de utilización) = ", p)
    print("Lq = ", lq)
    print("Wq = ", wq)
    print("Ws = ", ws)
    print("Ls = ", ls)

    more = 1
    while more != 2:
        more = int(input("Calcular probabilidad? Si = 1, No = 2  >> "))
        if more == 1:
            for i, function in enumerate(mm1_probs):
                for key, value in function.items():
                    if key == 'name':
                        print(i, value)

            selection = input(">> ")

            try:
                if int(selection) < 0 : raise ValueError
                print(mm1_probs[int(selection)]['function'](p, mu))
            except (ValueError, IndexError):
                pass

    input("Presiona [Enter] para continuar...")

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

def mms_cs(cc, s):
    return cc * s


def mms_cwls(cw, ls):
    return cw * ls

def mms():
    lamda = float(input("Escribe el valor de Lambda: "))
    mu = float(input("Escribe el valor de mu: "))
    s = float(input("Escribe el valor de s (número de servidores): "))
    cc = float(input("Escribe el valor de cc: "))
    cw = float(input("Escribe el valor de cw: "))
    p = lamda / (s*mu)
    p0 = mms_p0(lamda, mu, s, p)
    lq = mms_lq(lamda, mu, s, p0, p)
    wq = mms_wq(lq, lamda)
    ws = mms_ws(wq, mu)
    ls = mms_ls(lamda, ws)
    cs = mms_cs(cc, s)
    cwls = mms_cwls(cw, ls)
    ct = cs + cwls
    print("P0 = ", p0)
    print("Lq = ", lq)
    print("Wq = ", wq)
    print("Ws = ", ws)
    print("Ls = ", ls)
    print("Cs = ", cs)
    print("Cwls = ", cwls)
    print("CT = ", ct)

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
