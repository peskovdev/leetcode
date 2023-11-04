package main

import "strings"

func countPrefixes(words []string, s string) int {
	var count int
	for _, word := range words {
		if strings.HasPrefix(s, word) {
			count++
		}
	}
	return count
}
