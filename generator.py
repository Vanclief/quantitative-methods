#!/usr/bin/env python

import os
import sys
import math

def mcm(seed):
  ans = math.pow(seed, 2)
  return ans

def gcl_formula(m, a, c, z, n):
	ans = z
	for i in range(n):
		ans = ((a*ans+c) % m)
		print(i+1, " | ", ans, " | ", ans / m)

def gcl():
	m = int(input("Valor de m: "))
	a = int(input("Valor de a: "))
	c = int(input("Valor de c: "))
	z = int(input("Valor de Z0: "))
	n = int(input("Cantidad de números aleatorios: "))

	print("Itr | Z | R")
	gcl_formula(m, a, c, z, n)

	input("Presiona [Enter] para continuar...")


def exit():
	sys.exit()

generators = [
				{		"name": "Método de cuadrados medios",
						"function": mcm},
				{		"name": "Generador Congruencial Lineal",
						"function": gcl},
				{		"name": "Exit", "function": exit}
				]

def main():
	while True:
		os.system('clear')
		for i, generator in enumerate(generators):
			for key, value in generator.items():
				if key == 'name':
					print(i, value)

		selection = input(">> ")

		try:
			if int(selection) < 0 : raise ValueError

			generators[int(selection)]['function']()

		except(ValueError, IndexError):
			pass

if __name__ == "__main__":
    main()