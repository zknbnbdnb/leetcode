/*
 * @lc app=leetcode.cn id=2545 lang=golang
 *
 * [2545] 根据第 K 场考试的分数排序
 */

// @lc code=start
func sortTheStudents(score [][]int, k int) [][]int {
	sort.Slice(score, func(i, j int) bool {
		return score[i][k] > score[j][k]
	})
	return score

}

// @lc code=end

