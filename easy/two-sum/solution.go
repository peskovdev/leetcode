package main

func twoSum(nums []int, target int) []int {
	mp := map[int]int{}

	for i, n := range nums {
		if idx, ok := mp[target-n]; ok {
			return []int{idx, i}
		}

		mp[n] = i
	}

	return []int{-1, -1}
}
