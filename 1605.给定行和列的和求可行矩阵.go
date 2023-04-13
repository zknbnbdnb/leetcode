/*
 * @lc app=leetcode.cn id=1605 lang=golang
 *
 * [1605] 给定行和列的和求可行矩阵
 */

// @lc code=start
func restoreMatrix(rowSum []int, colSum []int) [][]int {
	m, n := len(rowSum), len(colSum)
	ans := make([][]int, m)
	for i := range ans {
		ans[i] = make([]int, n)
	}
	for i := 0; i < m; i++ {
		for j := 0; j < n; j++ {
			ans[i][j] = min(rowSum[i], colSum[j])
			rowSum[i] -= ans[i][j]
			colSum[j] -= ans[i][j]
		}
	}
	return ans

}
func min(a, b int) int {
	if a < b {
		return a
	}
	return b
}

// @lc code=end

