/*
 * @lc app=leetcode.cn id=1877 lang=golang
 *
 * [1877] 数组中最大数对和的最小值
 */

// @lc code=start
func minPairSum(nums []int) int {
	sort.Ints(nums)
	n := len(nums)
	ans := 0
	for i := 0; i < n/2; i++ {
		ans = max(ans, nums[i]+nums[n-i-1])
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

