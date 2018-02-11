#!/usr/bin/env python

import os
import sys
import time
import math

# Fórmulas generales

def factorial(n):

    i = 1
    factorial = 1

    while(i <= n):
        factorial *= i
        i += 1

    return factorial

def combinatory(n, k):

    subs = n - k
    return (factorial(n)) / (factorial(k) * factorial(subs))


def standard_deviation(variance):
    return math.sqrt(variance)

def general():
    print("Escriba los valores de x separados por un espacio: ")
    xs = [int(i) for i in input().split(' ')]
    print("Escriba los valores de las probabilidades de x (p(x)) separadas por un espacio: ")
    ps = [float(i) for i in input().split(' ')]

    media = sum(xs[i] * ps[i] for i in range(len(xs)))
    varianza = sum(pow(xs[i] - media, 2) * ps[i] for i in range(len(xs)))
    dev = standard_deviation(varianza)

    print('Media: {0} Varianza: {1} Desviación: {2}'.format(
        media,
        varianza,
        dev
        ))

    input("Presiona [Enter] para continuar...")

# Distribución uniforme discreta

def d_sum():

    i = float(input("Ingresa el rango inferior de la sumatoria:"))
    n = float(input("Ingresa el rango superior de la sumatoria:"))

    media = discrete_media(i, n)
    variance = discrete_variance(i, n, media)
    deviation = standard_deviation(variance)

    print('Media: {0} Varianza: {1} Desviación: {2}'.format(
        media,
        variance,
        deviation
        ))

    input("Presiona [Enter] para continuar...")

def d_average():

    n = float(input("Ingrese el numero de posibles casos: "))
    ans = 1 / n
    print("La posibilidad es:", ans)

    input("Presiona [Enter] para continuar...")

distribution_ops = {
        1 : d_sum,
        2 : d_average,
        }

def distribution():
    print("Distrubución Uniforme")
    print("1. Calcular Probailidad, Media y Varianza")
    print("2. Calcular Probabilidad")
    op = int(input(">> "))

    distribution_ops[op]()


def discrete_media(i, n):

    media = 0

    while (i < n):
        media += (i/n)
        i += 1

    return media

def discrete_variance(i, n, media):

    variance = 0

    while(i <= n):
        sub = i - media
        variance += (math.pow(sub, 2) / n)
        i += 1

    return variance

# Distribución binomial

def b_lambda():
    n = int(input("Número de pruebas (n): "))
    k = int(input("Numero de éxitos (k): "))
    p = float(input("Probabilidad de éxito (p): "))

    media = n * p
    variance = n * p * q

    prob = b_formula(n, k, p)

    print('Probabilidad:' , prob)
    print('Media: {0} Varianza: {1} Desviación: {2}'.format(
        media, variance, standard_deviation(variance)))


def b_formula(n, k, p):

    q = 1 - p
    subs = n - k

    return combinatory(n, k) * math.pow(p, k) * math.pow(q, subs)


def b_acum():
    inf = int(input("Límite inferior: "))
    sup = int(input("Límite superior: "))
    n = int(input("Número de pruebas (n): "))
    p = float(input("Probabilidad de éxito (p): "))

    acum = sum(b_formula(n, i, p) for i in range(inf, sup + 1))
    print("Acumulada", acum)


binomial_ops = {
        1 : b_lambda,
        2 : b_acum,
        }


def binomial_distribution():
    print("Distrubución Binomial")
    print("1. Calcular Probailidad, Media y Varianza")
    print("2. Calcular Acumulativa")
    op = int(input(">> "))

    binomial_ops[op]()


    op = int(input(">> "))
    input("Presiona [Enter] para continuar...")


# Poisson distribution

def p_lambda():
    n = int(input("Valor de n: "))
    p = int(input("Valor de p: "))
    print("Lambda = n * p")
    return [n*p, n*p]

def poisson_formula(x, l):
    up = math.exp(-l) * pow(l,x)
    down = math.factorial(x)
    return up/down

def p_prob():
    l = float(input("Valor de lambda: "))
    x = int(input("Valor de x: "))
    return [round(poisson_formula(x, l), 5) * 100 , l]

def p_acum():
    inf = int(input("Límite inferior: "))
    sup = int(input("Límite superior: "))
    l = float(input("Valor de lambda: "))
    res = sum(poisson_formula(i, l) for i in range(inf, sup + 1))
    return [round(res, 5) * 100 , l]


poisson_ops = {
        1 : p_lambda,
        2 : p_prob,
        3 : p_acum,
        }

def poisson_distribution():
    print("Distrubución de Poisson")
    print("Media = Varianza = Lambda")
    print("1. Calcular Lambda")
    print("2. Calcular Probabilidad")
    print("3. Calcular Acumulativa")
    op = int(input(">> "))

    res = poisson_ops[op]()
    print("Resultado: ", res[0])
    print('Media: {0} Varianza: {1} Desviación: {2}'.format(
        res[1],
        res[1],
        standard_deviation(res[1])
        ))

    input("Presiona [Enter] para continuar...")

# Distribución exponencial

def exp_formula(x,l):
    a = math.exp(-l * x)
    return 1 - a

def exp_prob(l):
    x = int(input("Valor de x: "))
    return round(exp_formula(x, l), 5) * 100

def exp_acum(l):
    inf = int(input("Límite inferior: "))
    sup = int(input("Límite superior: "))
    res = exp_formula(sup, l) - exp_formula(inf, l)
    return round(res, 5) * 100


expo_ops = {
        1 : exp_prob,
        2 : exp_acum,
        }

def exponential_distribution():
    print("Distribución Exponencial")
    print("Media = 1/lambda   Varianza = 1/lambda^2")
    print("1. Calcular Probabilidad")
    print("2. Calcular Acumulativa")
    op = int(input(">> "))

    l = float(input("Valor de Lambda: "))
    media = (1/l)
    varianza = (1 / pow(l,2))
    res = expo_ops[op](l)
    print("Resultado: ", res)
    print('Media: {0} Varianza: {1} Desviación: {2}'.format(
        media,
        varianza,
        standard_deviation(varianza)
        ))

    input("Presiona [Enter] para continuar...")

def exit():
    sys.exit()


functions = [
        {   "name": "Fórmulas generales (media, varianza, devest)",
            "function": general },
        {   "name": "Distribución Uniforme Discreta",
            "function": distribution },
        {   "name": "Distribución Binomial",
            "function": binomial_distribution },
        {   "name": "Distribución de Poisson",
            "function": poisson_distribution },
        {   "name": "Distribución exponencial",
            "function": exponential_distribution },
        { "name": "Exit", "function": exit },
        ]


def main():

    while True:
        os.system('clear')

        for i, function in enumerate(functions):
            for key, value in function.items() :
                if key == 'name':
                    print (i, value)

        selection = input(">> ")

        try:
            if int(selection) < 0 : raise ValueError

            functions[int(selection)]['function']()

        except (ValueError, IndexError):
            pass

if __name__ == "__main__":
    main()
