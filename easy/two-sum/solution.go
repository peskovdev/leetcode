package main

func twoSum(nums []int, target int) []int {
	hashmap := make(map[int]int)
	for i, n := range nums {
		if idx, ok := hashmap[target-n]; ok {
			return []int{idx, i}
		} else {
			hashmap[n] = i
		}
	}
	return []int{-1, -1}
}
