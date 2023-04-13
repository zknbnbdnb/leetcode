/*
 * @lc app=leetcode.cn id=2279 lang=golang
 *
 * [2279] 装满石头的背包的最大数量
 */

// @lc code=start
func maximumBags(capacity []int, rocks []int, additionalRocks int) int {
	for i := range capacity {
		capacity[i] -= rocks[i]
	}
	sort.Ints(capacity)
	res := 0
	for i := range capacity {
		if additionalRocks >= capacity[i] {
			additionalRocks -= capacity[i]
			res++
		} else {
			break
		}
	}
	return res
}

// @lc code=end

