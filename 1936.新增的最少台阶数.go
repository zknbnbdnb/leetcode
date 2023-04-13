/*
 * @lc app=leetcode.cn id=1936 lang=golang
 *
 * [1936] 新增的最少台阶数
 */

// @lc code=start
func addRungs(rungs []int, dist int) int {
	res, s := 0, 0
	for _, r := range rungs {
		if r-s > dist {
			res += (r - s - 1) / dist
		}
		s = r
	}
	return res

}

// @lc code=end

