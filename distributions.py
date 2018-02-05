#!/usr/bin/env python

import os
import sys

def distrubution():
    input("Ingresa el rango inferior de la sumatoria (i)")

def binomial_distribution():
    print
def poisson_distribution():
    print("Dist")
    input("Press [Enter] to continue...")

def exit():
    sys.exit()


functions = [
        {   "name": "Distrubución de probabilidad discreta general",
            "function": distribution },
        {   "name": "Distribución Binomial",
            "function": binomial_distribition },
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
