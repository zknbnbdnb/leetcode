/*
 * @lc app=leetcode.cn id=1626 lang=golang
 *
 * [1626] 无矛盾的最佳球队
 */

// @lc code=start
func bestTeamScore(scores []int, ages []int) int {
	n := len(scores)
	ans := 0
	dp := make([]int, n)
	idx := make([]int, n)
	for i := 0; i < n; i++ {
		idx[i] = i
	}
	sort.Slice(idx, func(i, j int) bool {
		if ages[idx[i]] == ages[idx[j]] {
			return scores[idx[i]] < scores[idx[j]]
		}
		return ages[idx[i]] < ages[idx[j]]
	})
	for i := 0; i < n; i++ {
		tmp := 0
		for j := 0; j < i; j++ {
			if scores[idx[i]] >= scores[idx[j]] {
				tmp = max(tmp, dp[j])
			}
		}
		dp[i] = tmp + scores[idx[i]]
		ans = max(ans, dp[i])
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

