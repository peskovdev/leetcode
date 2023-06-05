package main

func isPalindrome(s string) bool {
	for i := 0; i < len(s)/2; i++ {
		if s[i] != s[len(s)-1-i] {
			return false
		}
	}
	return true
}

func firstPalindrome(words []string) string {
	for _, word := range words {
		if isPalindrome(word) {
			return word
		}
	}
	return ""
}
