/*
 * @lc app=leetcode.cn id=1347 lang=golang
 *
 * [1347] 制造字母异位词的最小步骤数
 */

// @lc code=start
func minSteps(s string, t string) int {
	ds, dt := make(map[byte]int), make(map[byte]int)
	for i := 0; i < len(s); i++ {
		ds[s[i]]++
		dt[t[i]]++
	}
	res := 0
	for k, v := range ds {
		if tmp, ok := dt[k]; ok {
			res += max(0, v-tmp)
		} else {
			res += v
		}
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

