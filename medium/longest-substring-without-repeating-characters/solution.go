package main

func lengthOfLongestSubstring(s string) int {
	hashmap := make(map[byte]int)
	var lp, res int
	for rp := range s {
		hashmap[s[rp]]++
		for hashmap[s[rp]] >= 2 {
			hashmap[s[lp]]--
			lp++
		}
		if rp-lp+1 > res {
			res = rp - lp + 1
		}
	}
	return res
}
