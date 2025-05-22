package main

func isAnagram(s string, t string) bool {
	if len(s) != len(t) {
		return false
	}

	count := make(map[byte]int)

	for i := range len(s) {
		count[s[i]]++
		count[t[i]]--
	}

	for _, frequency := range count {
		if frequency != 0 {
			return false
		}
	}

	return true
}
