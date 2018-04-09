package main

import (
	"fmt"
	"log"
	"time"
	"math/rand"
	"gonum.org/v1/gonum/mat"
)

func randInt(min int, max int) int {
	return min + rand.Intn(max-min)
}

func calcP(n int, percent int) (p int) {

	div := float64(percent) / 100
	p = int(float64(n) * float64(n) * div)
	return p
}

func generateMatrix(n int)(matrix mat.Mutable) {
	return mat.NewDense(n, n, nil)
}

func fillMatrix(m mat.Mutable, n int, p int, mode int)(z mat.Mutable) {

	z = mat.NewDense(n, 1, nil)

	for i := 0; i < p; {
		// Create random number
		j := randInt(0, n)
		k := randInt(0, n)

		num := m.At(j, k)
		num2 := m.At(k, j)

		if (j != k && num != 1 && mode == 0) {
			// Set matrix to 1
			m.Set(j, k, 1)

			// Set vector counter to + 1
			x := z.At(j, 0)
			z.Set(j, 0, x+1)
			i += 1

		} else if (j != k && num != 1 && num2 !=1 &&  mode == 1) {
			// Set matrix to 1
			m.Set(j, k, 1)
			m.Set(k, j, 1)

			// Set vector counter to + 1
			x := z.At(j, 0)
			z.Set(j, 0, x+1)
			x = z.At(j, 0)
			z.Set(k, 0, x+1)
			i += 1
		}

	}

	return z
}

func printMaxAndMin(z mat.Mutable, n int)	{

	var maxRow, minRow int
	var maxVal, minVal float64

	maxVal, minVal = 0, 0 

	for l := 0; l < n; {

		val := z.At(l, 0)

		if (val > maxVal) {
			maxRow = l
			maxVal = val
		} 
		
		l += 1
	}

	minVal = maxVal
	
	for l := 0; l < n; { 

		val := z.At(l, 0)
		
		if (val < minVal) {
			minRow = l
			minVal = val
		}

		l += 1
	}

	fmt.Println("Fila con más 1s:")
	fmt.Println(maxRow + 1)
	fmt.Println("Fila con menos 1s:")
	fmt.Println(minRow + 1)
}


func matPrint(X mat.Mutable) {
	fa := mat.Formatted(X, mat.Prefix(""), mat.Squeeze())
	fmt.Printf("%v\n", fa)
}

func main() {

	rand.Seed(time.Now().UTC().UnixNano())

	var n, percent, mode int

	fmt.Println("Ingrese n:")
	_, err := fmt.Scanf("%d", &n)
	if err != nil {
		log.Fatal(err)
	}

	fmt.Println("Ingrese %:")
	_, err = fmt.Scanf("%d", &percent)
	if err != nil {
		log.Fatal(err)
	}

	fmt.Println("Ingrese 0 para matriz A o 1 para matriz B:")
	_, err = fmt.Scanf("%d", &mode)
	if err != nil {
		log.Fatal(err)
	}

	p := calcP(n, percent)

	matrix := generateMatrix(n)
	vector := fillMatrix(matrix, n, p, mode)
	matPrint(matrix)
	fmt.Println("Matrix count:")
	matPrint(vector)
	printMaxAndMin(vector, n)
}

