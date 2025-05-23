package main

type void struct{}

func longestConsecutive(nums []int) int {
	set := make(map[int]void, len(nums))
	for _, n := range nums {
		set[n] = void{}
	}

	res := 0
	for n := range set {
		tmp := 1
		prev := n - 1
		for _, ok := set[prev]; ok; _, ok = set[prev] {
			delete(set, prev)
			prev--
			tmp++
		}

		next := n + 1
		for _, ok := set[next]; ok; _, ok = set[next] {
			delete(set, next)
			tmp++
			next++
		}
		delete(set, n)
		res = max(res, tmp)
	}

	return res
}
