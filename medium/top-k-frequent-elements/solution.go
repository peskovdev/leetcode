package main

func topKFrequent(nums []int, k int) []int {
	count := make(map[int]int)
	for _, n := range nums {
		count[n]++
	}
	buckets := make([][]int, len(nums)+1)
	for n, freq := range count {
		buckets[freq] = append(buckets[freq], n)
	}
	var res []int
	for i := len(buckets) - 1; i >= 0; i-- {
		for _, n := range buckets[i] {
			res = append(res, n)
			if len(res) == k {
				return res
			}
		}
	}
	return res
}
