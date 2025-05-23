package main

type void struct{}

func longestConsecutive(nums []int) int {
	set := make(map[int]void, len(nums))
	for _, n := range nums {
		set[n] = void{}
	}

	res := 0
	for n := range set {
		if _, notLeft := set[n-1]; notLeft {
			continue
		}

		cur := 0
		for _, ok := set[n]; ok; _, ok = set[n] {
			cur++
			n++
		}
		res = max(res, cur)
	}

	return res
}
