/*
 * @lc app=leetcode.cn id=2125 lang=golang
 *
 * [2125] 银行中的激光束数量
 */

// @lc code=start
func numberOfBeams(bank []string) int {
	res := 0
	tmp := []int{}
	for i := 0; i < len(bank); i++ {
		j := strings.Count(bank[i], "1")
		if j > 0 {
			tmp = append(tmp, j)
		}
	}
	for i := 0; i < len(tmp)-1; i++ {
		res += tmp[i] * tmp[i+1]
	}
	return res

}

// @lc code=end

