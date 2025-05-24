package main

import "slices"

func threeSum(nums []int) [][]int {
	res := [][]int{}
	slices.Sort(nums)
	for i, target := range nums {
		if i > 0 && target == nums[i-1] {
			continue
		}

		lp, rp := i+1, len(nums)-1

		for lp < rp {
			cur := target + nums[lp] + nums[rp]

			if cur < 0 {
				lp++
			} else if cur > 0 {
				rp--
			} else {
				res = append(res, []int{target, nums[lp], nums[rp]})
				lp++
				for lp < rp && nums[lp] == nums[lp-1] {
					lp++
				}
			}
		}
	}

	return res
}
