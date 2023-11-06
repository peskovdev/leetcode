package main

import "fmt"

func main() {
	fmt.Println((1 + 4) / 2)
}

func search(nums []int, target int) int {
	lp, rp := 0, len(nums)-1
	for lp <= rp {
		mid := (lp + rp) / 2
		if target > nums[mid] {
			lp = mid + 1
		} else if target < nums[mid] {
			rp = mid - 1
		} else {
			return mid
		}
	}
	return -1
}
