/*
 * @lc app=leetcode.cn id=1282 lang=golang
 *
 * [1282] 用户分组
 */

// @lc code=start
func groupThePeople(groupSizes []int) [][]int {
	n := len(groupSizes)
	groups := make(map[int][]int)
	for i, v := range groupSizes {
		groups[v] = append(groups[v], i)
	}
	ans := make([][]int, 0)
	for k, v := range groups {
		for i := 0; i < len(v); i += k {
			ans = append(ans, v[i:i+k])
		}
	}
	return ans

}

// @lc code=end

