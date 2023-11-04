package main

import "reflect"

func containsPattern(arr []int, m int, k int) bool {
	for i := 0; i <= len(arr)-m; i += 1 {
		pattern := arr[i:(i + m)]
		counter := 1
		for j := i + m; j <= len(arr)-m; j += m {
			compared_pattern := arr[j : j+m]
			if !reflect.DeepEqual(pattern, compared_pattern) {
				break
			}
			counter++
			if counter == k {
				return true
			}
		}
	}
	return false
}
