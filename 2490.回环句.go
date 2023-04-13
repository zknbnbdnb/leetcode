/*
 * @lc app=leetcode.cn id=2490 lang=golang
 *
 * [2490] 回环句
 */

// @lc code=start
func isCircularSentence(sentence string) bool {
	s_list := strings.Split(sentence, " ")
	n := len(s_list)
	for i := 0; i < n-1; i++ {
		if s_list[i][len(s_list[i])-1] != s_list[i+1][0] {
			return false
		}
	}
	if s_list[n-1][len(s_list[n-1])-1] != s_list[0][0] {
		return false
	}
	return true

}

// @lc code=end

