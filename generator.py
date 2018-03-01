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
def arm_2x():
	m = 2
	a = 0
	b = 1
	count = 0
	lim = int(input("Cuántos números quieres generar?: "))
	print("# aceptado | # aleatorio")
	while count < lim:
		r1 = random.random()
		r2 = random.random()
		x = a + (b-a)*r1
		fx = 2*x
		if(r2 <= fx/m):
			count = count+1
			print(count, " | ", x)
	
	input("Presiona [Enter] para continuar...")

# Usando la función f(x) = 2x para el rango de 0 a 1 inclusivo
def arm_2f():
	print("f(x; [2,6]) = -1/6 + x/12")
	print("f(x; [6,8]) = 4/3 - x/6\n\n")
	m = 1/3
	a = 2
	b = 8
	count = itr = avg = s = 0
	min_x = b
	max_x = a
	x = []
	lim = int(input("Cuántos números quieres generar?: "))

	print("Itr | # aceptado | # aleatorio")
	while count < lim:
		r1 = random.random()
		r2 = random.random()
		x_s = a + (b-a)*r1
		if(x_s < 6):
			fx = x_s/12 - 1/6
		else:
			fx = 4/3 - x_s/6

		if(r2 <= fx/m):
			x.append(x_s)
			count = count+1
			max_x = x_s if x_s > max_x else max_x 
			min_x = x_s if x_s < min_x else min_x 
			avg = avg + x_s

			print(itr, " | ", count, " | ", "%.4f" % x_s)
		
		itr = itr+1
	
	avg = avg/count
	for i in x:
		s = s + pow(i - avg, 2)
	
	s = s/count

	print("Se aceptó un ", "%.4f" % (100*count/itr), "% de números")
	print("El máximo número generado fue ", "%.4f" % max_x)
	print("El mínimo número generado fue ", "%.4f" % min_x)
	print("El promedio de los números aceptados es: ", "%.4f" % avg)
	print("La varianza de los números aceptados es: ", "%.4f" % s)
	print("La desviación estándar de los números aceptados es: ", "%.4f" % math.sqrt(s))

	input("Presiona [Enter] para continuar...")


def t_inv():
	a = 1000
	b = 1500
	print('a = ', a)
	print('b = ', b)
	print("Itr | x")
	for i in range(0,100):
		r = random.random()
		x = a + r*(b-a)
		print(i+1,' |', x)

	input("Presiona [Enter] para continuar...")

def exit():
	sys.exit()

generators = [
				{		"name": "Método de cuadrados medios",
						"function": mcm},
				{		"name": "Generador Congruencial Lineal",
						"function": gcl},
				{		"name": "Método de aceptación y rechazo -> f(x; [0,1]) = 2x",
						"function": arm_2x},
				{		"name": "Método de aceptación y rechazo -> 2 funciones",
						"function": arm_2f},
				{		"name": "Método de la transformada inversa",
						"function": t_inv},
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