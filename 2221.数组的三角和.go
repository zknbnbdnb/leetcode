/*
 * @lc app=leetcode.cn id=2221 lang=golang
 *
 * [2221] 数组的三角和
 */

// @lc code=start
func triangularSum(nums []int) int {
	for n := len(nums) - 1; n > 0; n-- {
		for i := 0; i < n; i++ {
			a[i] = (a[i] + a[i+1]) % 10
		}
	}
	return a[0]
}

// @lc code=end

