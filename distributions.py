#!/usr/bin/env python

import os
import sys
import math

def distribution():
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


def standard_deviation(variance):
    return math.sqrt(variance)


def binomial_distribution():
    print("Dist")

def poisson_distribution():
    print("Dist")
    input("Press [Enter] to continue...")

def exit():
    sys.exit()


functions = [
        {   "name": "Distrubución de probabilidad discreta general",
            "function": distribution },
        {   "name": "Distribución Binomial",
            "function": binomial_distribution },
        {   "name": "Distribución de Poisson",
            "function": poisson_distribution },
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
