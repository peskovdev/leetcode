package main

func numIslands(grid [][]byte) int {
	var mark func(r, c int)
	mark = func(r, c int) {
		if (r >= 0 && r < len(grid)) &&
			(c >= 0 && c < len(grid[0])) &&
			grid[r][c] == '1' {
			grid[r][c] = '0'
			mark(r+1, c)
			mark(r-1, c)
			mark(r, c+1)
			mark(r, c-1)
		}
	}
	var res int
	for row := range grid {
		for col := range grid[row] {
			if grid[row][col] == '1' {
				mark(row, col)
				res += 1
			}
		}
	}
	return res
}
