package main

func isAnagram(s string, t string) bool {
	count := make(map[rune]int)
	for _, r := range s {
		count[r]++
	}
	for _, r := range t {
		count[r]--

	}
	for _, freq := range count {
		if freq != 0 {
			return false
		}
	}
	return true
}
