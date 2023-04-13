/*
 * @lc app=leetcode.cn id=2270 lang=golang
 *
 * [2270] 分割数组的方案数
 */

// @lc code=start
func waysToSplitArray(nums []int) int {
	l, r := nums[0], sumOfArray(nums)-nums[0]
	ans := 0
	if l >= r {
		ans = 1
	}
	for i := 1; i < len(nums)-1; i++ {
		l += nums[i]
		r -= nums[i]
		if l >= r {
			ans++
		}
	}
	return ans

}
func sumOfArray(nums []int) int {
	sum := 0
	for _, v := range nums {
		sum += v
	}
	return sum
}

// @lc code=end

