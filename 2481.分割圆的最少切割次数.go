/*
 * @lc app=leetcode.cn id=2481 lang=golang
 *
 * [2481] 分割圆的最少切割次数
 */

// @lc code=start
func numberOfCuts(n int) int {
	if n == 1 {
		return 0
	}
	if n%2 == 1 {
		return n
	} else {
		return n / 2
	}
}

// @lc code=end

