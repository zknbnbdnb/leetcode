/*
 * @lc app=leetcode.cn id=2582 lang=golang
 *
 * [2582] 递枕头
 */

// @lc code=start
func passThePillow(n int, time int) int {
	t := time % (2*n - 2)
	if t < n {
		return t + 1
	}
	return n - (t % n) - 1

}

// @lc code=end

