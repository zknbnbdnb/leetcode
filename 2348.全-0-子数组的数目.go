/*
 * @lc app=leetcode.cn id=2348 lang=golang
 *
 * [2348] 全 0 子数组的数目
 */

// @lc code=start
func zeroFilledSubarray(nums []int) int64 {
	ans := 0
	t := 0
	for _, v := range nums {
		if v == 0 {
			t++
			ans += t
		} else {
			t = 0
		}
	}
	return int64(ans)
}

// @lc code=end

