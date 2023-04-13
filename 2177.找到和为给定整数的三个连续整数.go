/*
 * @lc app=leetcode.cn id=2177 lang=golang
 *
 * [2177] 找到和为给定整数的三个连续整数
 */

// @lc code=start
func sumOfThree(num int64) []int64 {
	if num%3 != 0 {
		return []int64{}
	}
	return []int64{num/3 - 1, num / 3, num/3 + 1}

}

// @lc code=end

