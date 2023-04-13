/*
 * @lc app=leetcode.cn id=2554 lang=golang
 *
 * [2554] 从一个范围内选择最多整数 I
 */

// @lc code=start
func maxCount(banned []int, n int, maxSum int) int {
	db := make([]bool, n+1)
	for _, v := range banned {
		if v <= n {
			db[v] = true
		}
	}
	sum, ans := 0, 0
	for i := 1; i <= n; i++ {
		if !db[i] {
			sum += i
			if sum > maxSum {
				break
			}
			ans++
		}
	}
	return ans

}

// @lc code=end

