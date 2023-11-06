package main

func trap(height []int) int {
	var res int
	maxL, maxR := height[0], height[len(height)-1]
	lp, rp := 1, len(height)-2
	for lp <= rp {
		if maxL < maxR {
			if maxL-height[lp] > 0 {
				res += maxL - height[lp]
			}
			if height[lp] > maxL {
				maxL = height[lp]
			}
			lp++
		} else {
			if maxR-height[rp] > 0 {
				res += maxR - height[rp]
			}
			if height[rp] > maxR {
				maxR = height[rp]
			}
			rp--
		}
	}
	return res
}
