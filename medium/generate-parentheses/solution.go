package main

func generateParenthesis(n int) []string {
	res := []string{}

	var backtrack func(string, int, int)
	backtrack = func(chars string, opened, closed int) {
		if opened == closed && opened == n {
			res = append(res, chars)
			return
		}

		if opened != n {
			backtrack(chars+"(", opened+1, closed)
		}

		if closed < opened {
			backtrack(chars+")", opened, closed+1)
		}
	}

	backtrack("", 0, 0)
	return res
}
