package main

func isValid(s string) bool {
	bracketPair := map[byte]byte{')': '(', ']': '[', '}': '{'}
	var stack []byte
	for i := range s {
		if open, isClosed := bracketPair[s[i]]; isClosed {
			if len(stack) == 0 || stack[len(stack)-1] != open {
				return false
			}
			stack = stack[:len(stack)-1]
		} else {
			stack = append(stack, s[i])
		}
	}
	return len(stack) == 0
}
