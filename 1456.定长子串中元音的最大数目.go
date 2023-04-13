/*
 * @lc app=leetcode.cn id=1456 lang=golang
 *
 * [1456] 定长子串中元音的最大数目
 */

// @lc code=start
func maxVowels(s string, k int) int {
	vowels := map[byte]bool{
		'a': true,
		'e': true,
		'i': true,
		'o': true,
		'u': true,
	}
	n := len(s)
	count := 0
	for i := 0; i < k; i++ {
		if _, ok := vowels[s[i]]; ok {
			count++
		}
	}
	max_count := count
	for i := k; i < n; i++ {
		if _, ok := vowels[s[i]]; ok {
			count++
		}
		if _, ok := vowels[s[i-k]]; ok {
			count--
		}
		if count > max_count {
			max_count = count
		}
	}
	return max_count
}

// @lc code=end

