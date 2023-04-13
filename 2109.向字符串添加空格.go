/*
 * @lc app=leetcode.cn id=2109 lang=golang
 *
 * [2109] 向字符串添加空格
 */

// @lc code=start
func addSpaces(s string, spaces []int) string {
	sb := strings.Builder{}
	idx := 0
	for i := 0; i < len(s); i++ {
		if idx < len(spaces) && i == spaces[idx] {
			sb.WriteByte(' ')
			idx++
		}
		sb.WriteByte(s[i])
	}
	return sb.String()

}

// @lc code=end

