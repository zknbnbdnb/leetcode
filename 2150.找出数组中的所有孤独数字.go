/*
 * @lc app=leetcode.cn id=2150 lang=golang
 *
 * [2150] 找出数组中的所有孤独数字
 */

// @lc code=start
func findLonely(nums []int) []int {
	res := []int{}
	d := make(map[int]int)
	for _, v := range nums {
		d[v]++
	}
	for k, v := range d {
		_, ok1 := d[k-1]
		_, ok2 := d[k+1]
		if !ok1 && !ok2 && v == 1 {
			res = append(res, k)
		}
	}
	return res

}

// @lc code=end

