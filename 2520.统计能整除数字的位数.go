/*
 * @lc app=leetcode.cn id=2520 lang=golang
 *
 * [2520] 统计能整除数字的位数
 */

// @lc code=start
func countDigits(num int) int {
	res := 0
	tmp := strconv.Itoa(num)
	for i := 0; i < len(tmp); i++ {
		if num%(int(tmp[i])-48) == 0 { // 48 is the ASCII code of '0'
			res++
		}
	}
	return res

}

// @lc code=end

