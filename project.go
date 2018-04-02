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

func fillMatrix(m mat.Mutable, n int, p int) {
	for i := 0; i < p; {
		// Create random number
		j := randInt(0, n)
		k := randInt(0, n)
		num := m.At(j, k)

		if (j != k && num != 1) {
			m.Set(j, k, 1)
			i += 1
		}
	}
}

func matPrint(X mat.Mutable) {
	fa := mat.Formatted(X, mat.Prefix(""), mat.Squeeze())
	fmt.Printf("%v\n", fa)
}

func main() {

	rand.Seed(time.Now().UTC().UnixNano())

	var n, percent int

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

	p := calcP(n, percent)

	matrix := generateMatrix(n)
	fillMatrix(matrix, n, p)
	matPrint(matrix)
}

