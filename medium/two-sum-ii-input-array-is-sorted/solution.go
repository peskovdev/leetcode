package main

func twoSum(numbers []int, target int) []int {
	lp, rp := 0, len(numbers)-1
	for lp < rp {
		cur := numbers[lp] + numbers[rp]
		if cur < target {
			lp++
		} else if cur > target {
			rp--
		} else {
			return []int{lp + 1, rp + 1}
		}
	}
	return []int{-1, -1}
}
