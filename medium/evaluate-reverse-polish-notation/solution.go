package main

import "strconv"

func evalRPN(tokens []string) int {
	operations := map[string]func(a, b int) int{
		"+": func(a, b int) int { return a + b },
		"-": func(a, b int) int { return a - b },
		"*": func(a, b int) int { return a * b },
		"/": func(a, b int) int { return a / b },
	}

	stack := []int{}
	for _, token := range tokens {
		if calculate, ok := operations[token]; ok {
			a, b := stack[len(stack)-2], stack[len(stack)-1]
			stack = append(stack[:len(stack)-2], calculate(a, b))
		} else {
			val, _ := strconv.Atoi(token)
			stack = append(stack, val)
		}
	}

	return stack[0]
}
