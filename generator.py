#!/usr/bin/env python

import os
import sys
import math
import random

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

# Usando la función f(x) = 2x para el rango de 0 a 1 inclusivo
def arm():
	m = 2
	a = 0
	b = 1
	count = 0
	print("Itr | Número")
	while count < 5000:
		r1 = random.random()
		r2 = random.random()
		x = a + (b-a)*r1
		fx = 2*x
		if(r2 <= fx/m):
			count = count+1
			print(count, " | ", x)
	
	input("Presiona [Enter] para continuar...")


def exit():
	sys.exit()

generators = [
				{		"name": "Método de cuadrados medios",
						"function": mcm},
				{		"name": "Generador Congruencial Lineal",
						"function": gcl},
				{		"name": "Método de aceptación y rechazo",
						"function": arm},
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