package main

import "fmt"

func is_even(n int) (eveness bool) {
	return n%2 == 0
}

func max(a int, b int) (result int) {
	if a > b {
		return a
	}
	return b
}

func Solver3nPlus1(i int, j int) (max_cycles int) {
	result := 0
	for x := i; x < j; x++ {
		n := x
		current_cycle := 0
		for n != 1 {
			if is_even(n) {
				n = n / 2
			} else {
				n = (3 * n) + 1
			}
			current_cycle++
		}
		result = max(result, current_cycle)
	}
	return result + 1
}
func main() {
	fmt.Println(Solver3nPlus1(1, 10))
	fmt.Println(Solver3nPlus1(100, 200))
	fmt.Println(Solver3nPlus1(201, 210))
	fmt.Println(Solver3nPlus1(900, 1000))
}
