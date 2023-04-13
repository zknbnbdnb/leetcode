/*
 * @lc app=leetcode.cn id=1451 lang=golang
 *
 * [1451] 重新排列句子中的单词
 */

// @lc code=start
func arrangeWords(text string) string {
	words := strings.Split(text, " ")
	words[0] = strings.ToLower(words[0])
	sort.SliceStable(words, func(i, j int) bool {
		return len(words[i]) < len(words[j])
	})
	words[0] = strings.Title(words[0])
	return strings.Join(words, " ")

}

// @lc code=end

