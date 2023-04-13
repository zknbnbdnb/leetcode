/*
 * @lc app=leetcode.cn id=2525 lang=golang
 *
 * [2525] 根据规则将箱子分类
 */

// @lc code=start
func categorizeBox(length int, width int, height int, mass int) string {
	heavy, bulky := false, false
	if length >= 1e4 || width >= 1e4 || height >= 1e4 || (length*width*height) >= 1e9 {
		bulky = true
	}
	if mass >= 100 {
		heavy = true
	}
	if heavy && bulky {
		return "Both"
	}
	if heavy {
		return "Heavy"
	}
	if bulky {
		return "Bulky"
	}
	return "Neither"

}

// @lc code=end

