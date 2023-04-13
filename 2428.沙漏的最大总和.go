/*
 * @lc app=leetcode.cn id=2428 lang=golang
 *
 * [2428] 沙漏的最大总和
 */

// @lc code=start
func maxSum(grid [][]int) int {
	m, n := len(grid), len(grid[0])
	res := 0
	for i := 0; i < m-2; i++ {
		for j := 0; j < n-2; j++ {
			tmp := sumOfArray(grid[i][j:j+3]) + grid[i+1][j+1] + sumOfArray(grid[i+2][j:j+3]) - grid[i+1][j] - grid[i+1][j+2]
			res = max(res, tmp)
		}
	}
	return res

}
func sumOfArray(arr []int) int {
	res := 0
	for _, v := range arr {
		res += v
	}
	return res
}
func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}

// @lc code=end

