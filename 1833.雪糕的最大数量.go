/*
 * @lc app=leetcode.cn id=1833 lang=golang
 *
 * [1833] 雪糕的最大数量
 */

// @lc code=start
func maxIceCream(costs []int, coins int) int {
	sort.Ints(costs)
	res := 0
	for _, v := range costs {
		if coins >= v {
			coins -= v
			res++
		} else {
			break
		}
	}
	return res

}

// @lc code=end

