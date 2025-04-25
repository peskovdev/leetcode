package main

type hashibleMap [26]int

func groupAnagrams(strs []string) [][]string {
	groups := map[hashibleMap][]string{}

	for _, word := range strs {
		anagram := getAnagram(word)
		groups[anagram] = append(groups[anagram], word)
	}

	res := [][]string{}
	for _, words := range groups {
		res = append(res, words)
	}

	return res
}

func getAnagram(word string) hashibleMap {
	var count hashibleMap

	for _, char := range word {
		count[char-'a']++
	}

	return count
}
