package main

func largestRectangleArea(heights []int) int {
	var stack [][2]int //pair: idx, height
	var res int
	for i, h := range heights {
		if len(stack) != 0 && h < stack[len(stack)-1][1] {
			start := i
			for len(stack) > 0 && stack[len(stack)-1][1] > h {
				idx, height := stack[len(stack)-1][0], stack[len(stack)-1][1]
				square := height * (i - idx)
				if square > res {
					res = square
				}
				stack = stack[:len(stack)-1]
				start = idx
			}
			stack = append(stack, [2]int{start, h})
		} else {
			stack = append(stack, [2]int{i, h})
		}
	}
	for i := range stack {
		idx, height := stack[i][0], stack[i][1]
		square := height * (len(heights) - idx)
		if square > res {
			res = square
		}
	}
	return res
}
