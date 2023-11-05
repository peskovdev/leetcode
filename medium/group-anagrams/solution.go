package main

func groupAnagrams(strs []string) [][]string {
	groups := make(map[[26]byte][]string)
	for _, s := range strs {
		var count [26]byte
		for _, r := range s {
			count[r-'a']++
		}
		groups[count] = append(groups[count], s)
	}
	var res [][]string
	for _, group := range groups {
		res = append(res, group)
	}
	return res
}
