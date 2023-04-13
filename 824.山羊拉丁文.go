/*
 * @lc app=leetcode.cn id=824 lang=golang
 *
 * [824] 山羊拉丁文
 */

// @lc code=start
func toGoatLatin(sentence string) string {
	words := strings.Split(sentence, " ")
	for i, word := range words {
		if isVowel(word[0]) {
			words[i] = word + "ma"
		} else {
			words[i] = word[1:] + string(word[0]) + "ma"
		}
		words[i] += strings.Repeat("a", i+1)
	}
	return strings.Join(words, " ")

}
func isVowel(c byte) bool {
	return c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u' || c == 'A' || c == 'E' || c == 'I' || c == 'O' || c == 'U'
}

// @lc code=end

