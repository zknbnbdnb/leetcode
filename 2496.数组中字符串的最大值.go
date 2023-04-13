/*
 * @lc app=leetcode.cn id=2496 lang=golang
 *
 * [2496] 数组中字符串的最大值
 */

// @lc code=start
func maximumValue(strs []string) int {
	res := []int{}
	for _, v := range strs {
		t, err := strconv.Atoi(v)
		if err != nil {
			res = append(res, len(v))
		} else {
			res = append(res, t)
		}
	}
	return maxOfArray(res)

}
func maxOfArray(arr []int) int {
	res := 0
	for _, v := range arr {
		res = max(res, v)
	}
	return res
}
func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}

// @lc code=end

