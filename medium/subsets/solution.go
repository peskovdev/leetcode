package main

func subsets(nums []int) [][]int {
	var res [][]int
	var backtrack func(cur []int, start int)
	backtrack = func(cur []int, start int) {
		res = append(res, cur)
		for i := start; i < len(nums); i++ {
			updated := make([]int, len(cur), len(cur)+1)
			copy(updated, cur)
			updated = append(updated, nums[i])
			backtrack(updated, i+1)
		}
	}
	backtrack([]int{}, 0)
	return res
}
