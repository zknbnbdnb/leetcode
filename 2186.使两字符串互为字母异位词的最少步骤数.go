/*
 * @lc app=leetcode.cn id=2186 lang=golang
 *
 * [2186] 使两字符串互为字母异位词的最少步骤数
 */

// @lc code=start
func minSteps(s string, t string) int {
	res := 0
	str2cnt := make(map[rune]int)
	for _, v := range s {
		str2cnt[v]++
	}
	for _, v := range t {
		str2cnt[v]--
	}
	for _, v := range str2cnt {
		res += abs(v)
	return res
}
func abs(x int) int {
	if x < 0 {
		return -x
	}
	return x
}

// @lc code=end

