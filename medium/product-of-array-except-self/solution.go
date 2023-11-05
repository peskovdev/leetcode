package main

func productExceptSelf(nums []int) []int {
	res := make([]int, len(nums))
	res[0], res[len(nums)-1] = 1, 1
	for prSum, i := 1, 0; i < len(nums)-1; i++ {
		prSum *= nums[i]
		res[i+1] = prSum
	}
	for prSum, i := 1, len(nums)-1; i > 0; i-- {
		prSum *= nums[i]
		res[i-1] *= prSum
	}
	return res
}
