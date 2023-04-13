/*
 * @lc app=leetcode.cn id=2079 lang=golang
 *
 * [2079] 给植物浇水
 */

// @lc code=start
func wateringPlants(plants []int, capacity int) int {
	res, i := 0, 0
	c_capacity := capacity
	for i < len(plants) {
		if plants[i] <= capacity {
			res++
			capacity -= plants[i]
			i++
		} else {
			res += 2 * i
			capacity = c_capacity
		}
	}
	return res

}

// @lc code=end

