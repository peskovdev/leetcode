package main

func buddyStrings(s string, goal string) bool {
	if len(s) != len(goal) {
		return false
	}
	if s == goal {
		tmp := make(map[rune]int)
		for _, v := range s {
			tmp[v]++
			if tmp[v] >= 2 {return true}
		}
	}
   idx := []int{}
	for i := 0; i < len(s); i++ {
		if s[i] != goal[i] {
			idx = append(idx, i)
		}
	}
   return len(idx) == 2 && s[idx[0]] == goal[idx[1]] && s[idx[1]] == goal[idx[0]]
}
