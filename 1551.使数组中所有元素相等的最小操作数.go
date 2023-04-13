/*
 * @lc app=leetcode.cn id=1551 lang=golang
 *
 * [1551] 使数组中所有元素相等的最小操作数
 */

// @lc code=start
func minOperations(n int) int {
	if n%2 == 0 {
		return n * n / 4
	} else {
		t := (n + 1) / 2
		return t * (t - 1)
	}

}

// @lc code=end

