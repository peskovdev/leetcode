package main

import "unicode"

func isPalindrome(s string) bool {
	lp, rp := 0, len(s)-1
	for lp < rp {
		for lp < rp && !isAlNum(s[lp]) {
			lp++
		}
		for lp < rp && !isAlNum(s[rp]) {
			rp--
		}
		if unicode.ToLower(rune(s[lp])) != unicode.ToLower(rune(s[rp])) {
			return false
		}
		lp, rp = lp+1, rp-1
	}
	return true
}

func isAlNum(r byte) bool {
	return ('a' <= r && r <= 'z') || ('A' <= r && r <= 'Z') || ('0' <= r && r <= '9')
}
