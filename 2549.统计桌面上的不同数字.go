/*
 * @lc app=leetcode.cn id=2549 lang=golang
 *
 * [2549] 统计桌面上的不同数字
 */

// @lc code=start
func distinctIntegers(n int) int {
	if n == 1 {
		return 1
	} else {
		return n - 1
	}

}

// @lc code=end

