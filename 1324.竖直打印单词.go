/*
 * @lc app=leetcode.cn id=1324 lang=golang
 *
 * [1324] 竖直打印单词
 */

// @lc code=start
func printVertically(s string) []string {
	words := strings.Split(s, " ")
	maxLen := 0
	for _, word := range words {
		if len(word) > maxLen {
			maxLen = len(word)
		}
	}
	res := make([]string, maxLen)
	for i := 0; i < maxLen; i++ {
		for _, word := range words {
			if i < len(word) {
				res[i] += string(word[i])
			} else {
				res[i] += " "
			}
		}
	}
	for i := 0; i < maxLen; i++ {
		res[i] = strings.TrimRight(res[i], " ")
	}
	return res

}

// @lc code=end

