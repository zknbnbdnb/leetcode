/*
 * @lc app=leetcode.cn id=2379 lang=golang
 *
 * [2379] 得到 K 个黑块的最少涂色次数
 */

// @lc code=start
func minimumRecolors(blocks string, k int) int {
	i, j := 0, k-1
	n := len(blocks)
	res := []int{}
	for j < n {
		res = append(res, strings.Count(blocks[i:j+1], "W"))
		i++
		j++
	}
	return minOfArray(res)
}
func minOfArray(arr []int) int {
	min := arr[0]
	for _, v := range arr {
		if v < min {
			min = v
		}
	}
	return min
}

// @lc code=end

