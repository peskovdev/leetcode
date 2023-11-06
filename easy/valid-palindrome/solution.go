package main

import "unicode"

func isPalindrome(s string) bool {
	lp, rp := 0, len(s)-1
	for lp < rp {
		if !(unicode.IsNumber(rune(s[lp])) || unicode.IsLetter(rune(s[lp]))) {
			lp++
		} else if !(unicode.IsNumber(rune(s[rp])) || unicode.IsLetter(rune(s[rp]))) {
			rp--
		} else if unicode.ToLower(rune(s[lp])) != unicode.ToLower(rune(s[rp])) {
			return false
		} else {
			lp, rp = lp+1, rp-1
		}
	}
	return true
}
