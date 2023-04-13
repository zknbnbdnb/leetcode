/*
 * @lc app=leetcode.cn id=1615 lang=golang
 *
 * [1615] 最大网络秩
 */

// @lc code=start
func maximalNetworkRank(n int, roads [][]int) int {
	cnt := make([]int, n)
	g := make([][]int, n)
	for i := 0; i < n; i++ {
		g[i] = make([]int, n)
	}
	for _, road := range roads {
		cnt[road[0]]++
		cnt[road[1]]++
		g[road[0]][road[1]] = 1
		g[road[1]][road[0]] = 1
	}
	ans := 0
	for i := 0; i < n; i++ {
		for j := i + 1; j < n; j++ {
			ans = max(ans, cnt[i]+cnt[j]-g[i][j])
		}
	}
	return ans

}
func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}

// @lc code=end

